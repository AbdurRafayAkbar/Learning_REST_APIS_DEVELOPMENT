from django.shortcuts import render
from .models import Students
from .serializers import studentserializer
from rest_framework import generics

class StudentsList(generics.ListCreateAPIView):
    queryset=Students.objects.all()
    serializer_class = studentserializer

class SingleStudentList(generics.RetrieveUpdateDestroyAPIView):
    queryset=Students.objects.all()
    serializer_class=studentserializer