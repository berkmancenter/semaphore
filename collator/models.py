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