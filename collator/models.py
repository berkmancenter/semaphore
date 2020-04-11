from django.db import models

# Create your models here.
class Baz(models.Model):
    foo = models.CharField(max_length=50)
    bar = models.CharField(max_length=50)