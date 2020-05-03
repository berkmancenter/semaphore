# Add a referer header mirroring origin on specific requests.

# The Django CSRF Middleware checks secure requests' referer.  But, requests
# from an extension can't set a referer, nor do they automatically get one.  So,
# Django rejects the request.  This middleware checks to see if a request is
# missing the referer header, but coming with an approved origin.  If so, it
# uses the origin as referer so the CSRFViewMiddleware validates the request.

import logging
from django.conf import settings

logger = logging.getLogger()


class OriginAsRefererMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        referer = request.META.get('HTTP_REFERER')
        origin = request.META.get('HTTP_ORIGIN')
        host = request.META.get('HTTP_HOST')

        if (request.is_secure() and
            referer is None and
            origin in settings.CSRF_TRUSTED_ORIGINS):
            new_referer = "https://{}".format(host)
            logger.debug('setting referer to (secure) host', new_referer)
            request.META['HTTP_REFERER'] = new_referer
        logger.debug('foo')

        return self.get_response(request)
