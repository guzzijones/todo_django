from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


class ListTodos(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Create your views here.
