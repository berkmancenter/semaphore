import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from . import models


CREDENTIALS = {'username': 'imauser', 'password': 'secret'}
DATE = datetime.date.today()  # Yes, this could be flakey.


class SemaphoreModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username=CREDENTIALS['username'])
        self.user.set_password(CREDENTIALS['password'])
        self.user.save()

    def test_filter_by_date_and_queryset(self):
        self.assertEqual(
            models.RawFlag.on_date(DATE, models.RawFlag.objects.all()), 0)
        models.RawFlag.objects.create(
            flagger=self.user,
        )
        self.assertEqual(
            models.RawFlag.on_date(DATE, models.RawFlag.objects.all()), 1)
        self.assertEqual(
            models.RawFlag.on_date(
                DATE, models.RawFlag.objects.exclude(flagger=self.user)), 
            0
        )