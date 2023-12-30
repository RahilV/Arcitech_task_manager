# tasks/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Test Task', 'description': 'Test Description'}

    def test_create_task(self):
        url = reverse('task-create')
        response = self.client.post(url, self.task_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_list_tasks(self):
        Task.objects.create(title='Test Task', description='Test Description')
        url = reverse('task-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_retrieve_task(self):
        task = Task.objects.create(title='Test Task', description='Test Description')
        url = reverse('task-detail', args=[task.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        task = Task.objects.create(title='Test Task', description='Test Description')
        updated_data = {'title': 'Updated Task', 'description': 'Updated Description'}
        url = reverse('task-detail', args=[task.id])
        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=task.id).title, 'Updated Task')

    def test_delete_task(self):
        task = Task.objects.create(title='Test Task', description='Test Description')
        url = reverse('delete-task', args=[task.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
