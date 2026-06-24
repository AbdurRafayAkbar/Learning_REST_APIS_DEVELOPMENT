from django.shortcuts import render
from .models import Comments,Blogs
from .serializers import blog_serializer,comments_serializer
from rest_framework import generics

class Blog_presentaion(generics.CreateAPIView,generics.ListAPIView):
    queryset=Blogs.objects.all()
    serializer_class=blog_serializer

class Comments_presentation(generics.ListCreateAPIView):
    queryset=Comments.objects.all()
    serializer_class=comments_serializer