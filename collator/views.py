from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    return HttpResponse('{} raw flags.'.format(models.RawFlag.objects.count()))