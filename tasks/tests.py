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

    def create_task(self, title='Test Task', description='Test Description'):
        """Helper method to create a task."""
        return Task.objects.create(title=title, description=description)

    def test_create_task(self):
        """Test creating a new task."""

        url = reverse('task-create')

        response = self.client.post(url, self.task_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_list_tasks(self):
        """Test listing tasks."""

        self.create_task()
        url = reverse('task-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_retrieve_task(self):
        """Test retrieving a task."""

        task = self.create_task()
        url = reverse('task-detail', args=[task.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        """Test updating a task."""

        task = self.create_task()
        updated_data = {'title': 'Updated Task', 'description': 'Updated Description'}
        url = reverse('task-detail', args=[task.id])


        response = self.client.put(url, updated_data, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=task.id).title, 'Updated Task')

    def test_delete_task(self):
        """Test deleting a task."""

        task = self.create_task()
        url = reverse('delete-task', args=[task.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
