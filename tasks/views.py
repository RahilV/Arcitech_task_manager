from rest_framework import generics
from .serializers import *
from .models import *
from django.shortcuts import render
from django.views import View

class TaskManagerView(View):
    def get(self, request):
        return render(request, 'tasks_manager.html')

class ListTask(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DetailTask(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer