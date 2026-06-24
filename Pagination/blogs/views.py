from django.shortcuts import render
from rest_framework import generics
from .models import Blogs
from.serializers import Blog_Serializer

class Blogs_View(generics.ListCreateAPIView):
    queryset=Blogs.objects.all()
    serializer_class=Blog_Serializer

class Detailed_Blog_View(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blogs.objects.all()
    serializer_class=Blog_Serializer
    lookup_field="id"
