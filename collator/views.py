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
    return HttpResponse('Profile for {}.'.format(request.user.username))

# Graphs
def reports_per_day(request):
    # Dummy data
    num_days = 14
    max_count = 100
    data = {
        'max_count': max_count,
        'days': models.RawFlag.day_histogram(14)
    }
    return shortcuts.render(request, 'graphs/reports_per_day.html', data)