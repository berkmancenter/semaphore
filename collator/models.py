import datetime

from django.conf import settings
from django.db import models


# Create your models here.
class RawFlag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    flagger = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    language = models.CharField(max_length=10)
    reported_user_id = models.CharField(max_length=25)
    reported_tweet_id = models.CharField(max_length=25)

    @classmethod
    def on_date(cls, date, queryset):
        return queryset.filter(
            created__year=date.year,
            created__month=date.month,
            created__day=date.day,
        ).count()

    @classmethod
    def day_histogram(cls, num_days=14, filters=None):
        queryset = cls.objects.all()
        if filters:
            queryset = queryset.filter(**filters)
        histogram = [
            {
                'date': datetime.date.today() - datetime.timedelta(days=delta),
            } for delta in range(num_days-1, -1, -1)
        ]
        for day in histogram:
            day['count'] = cls.on_date(day['date'], queryset=queryset)
        max_count = max([day['count'] for day in histogram]) + 1
        for day in histogram:
            day['count_perc_of_max'] = 100.0 * day['count'] / max_count
        return histogram