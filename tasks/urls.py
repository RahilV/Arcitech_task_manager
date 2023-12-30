# tasks/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailTask.as_view(), name='task-detail'),
    path('list', ListTask.as_view(), name='task-list'),
    path('create', CreateTask.as_view(), name='task-create'),
    path('delete/<int:pk>/', DeleteTask.as_view(), name='delete-task'),
    path('', TaskManagerView.as_view(), name='task-manager')
]
