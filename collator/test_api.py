from http import HTTPStatus

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from . import models


# if this is changed, the extension also needs an update
FLAGGING_URL = '/api/v0/raw_flags/'
CREDENTIALS = {'username': 'flagger', 'password': 'secret'}


class SemaphoreAPITestCase(APITestCase):

    def setUp(self):
        user = User.objects.create(username=CREDENTIALS['username'])
        user.set_password(CREDENTIALS['password'])
        user.save()

    def test_unauthenticated_flagging_unauthorized(self):
        data = {
            'language': 'EN',
            'reported_user_id': '12345',
            'reported_tweet_id': '67890',
        }
        response = self.client.post(FLAGGING_URL, data, format='json')
        self.assertEqual(response.status_code,  HTTPStatus.FORBIDDEN)

    def test_authenticated_flagging_creates_raw_flag(self):
        self.assertEqual(models.RawFlag.objects.count(), 0)
        self.assertTrue(self.client.login(**CREDENTIALS))
        data = {
            'language': 'EN',
            'reported_user_id': '12345',
            'reported_tweet_id': '67890',
        }
        response = self.client.post(FLAGGING_URL, data, format='json')
        self.assertEqual(response.status_code,  HTTPStatus.CREATED)
        self.assertEqual(models.RawFlag.objects.count(), 1)