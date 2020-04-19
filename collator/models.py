from django.db import models

# Create your models here.
class RawFlag(models.Model):
    language = models.CharField(max_length=10)
    reported_user_id = models.CharField(max_length=12)
    reported_tweet_id = models.CharField(max_length=25)