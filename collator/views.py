from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    return HttpResponse('{} bazes.'.format(models.Baz.objects.count()))