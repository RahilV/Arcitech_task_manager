# tasks/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailTask.as_view()),
    path('list', ListTask.as_view()),
    path('create', CreateTask.as_view()),
    path('delete/<int:pk>', DeleteTask.as_view()),
    path('', TaskManagerView.as_view(), name='task-manager')
]
