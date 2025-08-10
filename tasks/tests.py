from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from bots.models import Bot
from .models import Task

class TaskAPITest(APITestCase):
    def setUp(self):
        self.bot = Bot.objects.create(name="Test Bot")
        self.task = Task.objects.create(bot=self.bot, command="echo Hello", status="in_progress")

    def test_list_tasks(self):
        url = reverse('task-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_task(self):
        url = reverse('task-list-create')
        data = {'bot': self.bot.id, 'command': 'echo Test'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['command'], 'echo Test')

    def test_get_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['command'], self.task.command)

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])
        data = {'command': 'echo Updated', 'bot': self.bot.id, 'status': 'done'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['command'], 'echo Updated')
        self.assertEqual(response.data['status'], 'done')

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
