# Add a referer header mirroring origin on specific requests

# The Django CSRF Middleware checks secure requests' referer.  But, requests
# from an extension can't set a referer, nor do they automatically get one.  So,
# Django rejects the request.  This middleware checks to see if a request is
# missing the referer header, but coming with an approved origin.  If so, it
# uses the origin as referer so the CSRFViewMiddleware validates the request.


class OriginAsRefererMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        referer = request.META.get('HTTP_REFERER')
        origin = request.META.get('HTTP_ORIGIN')
        print('ro:', referer, origin)
        if request.is_secure() and (referer is None) and origin:
            request.META['HTTP_REFERER'] = origin

        return self.get_response(request)