from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Bot

class BotAPITest(APITestCase):
    def setUp(self):
        self.bot = Bot.objects.create(name="Test Bot")

    def test_list_bots(self):
        url = reverse('bot-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_bot(self):
        url = reverse('bot-list-create')
        data = {'name': 'New Bot'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Bot')

    def test_get_bot(self):
        url = reverse('bot-detail', args=[self.bot.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.bot.name)

    def test_update_bot(self):
        url = reverse('bot-detail', args=[self.bot.id])
        data = {'name': 'Updated Bot'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Bot')

    def test_delete_bot(self):
        url = reverse('bot-detail', args=[self.bot.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
