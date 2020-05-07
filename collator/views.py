import datetime
import random

from django import shortcuts
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    return HttpResponse('{} raw flags.'.format(models.RawFlag.objects.count()))

@login_required
def profile(request):
    data = {
        'days': models.RawFlag.day_histogram(
            14, 
            filters={'flagger': request.user}
        ),
        'flags': models.RawFlag.objects.filter(
            flagger=request.user,
        ).order_by('-created'),
    }
    return shortcuts.render(request, 'profile.html', data)

# Graphs
def reports_per_day(request):
    data = {
        'days': models.RawFlag.day_histogram(14)
    }
    return shortcuts.render(request, 'graphs/reports_per_day.html', data)