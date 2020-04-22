from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    return HttpResponse('{} raw flags.'.format(models.RawFlag.objects.count()))

@login_required
def profile(request):
    return HttpResponse('Profile for {}.'.format(request.user.username))