# bot/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from bot.models import TelegramUser

class TelegramAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_upsert_create(self):
        url = reverse('user-upsert')
        data = {"telegram_id": 1001, "username": "user1"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['telegram_id'], 1001)

    def test_user_upsert_existing(self):
        TelegramUser.objects.create(telegram_id=1002)
        url = reverse('user-upsert')
        data = {"telegram_id": 1002}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['telegram_id'], 1002)

    def test_create_referral(self):
        TelegramUser.objects.create(telegram_id=2001)
        TelegramUser.objects.create(telegram_id=2002)
        url = reverse('create-referral')
        data = {"referrer_telegram_id": 2001, "referred_telegram_id": 2002}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['referrer_telegram_id'], 2001)

    def test_user_status(self):
        user = TelegramUser.objects.create(telegram_id=3001)
        url = reverse('user-status', args=[user.telegram_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['telegram_id'], 3001)

    def test_referral_summary(self):
        referrer = TelegramUser.objects.create(telegram_id=4001)
        referred = TelegramUser.objects.create(telegram_id=4002, referred_by=referrer)
        url = reverse('referral-summary', args=[referrer.telegram_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
