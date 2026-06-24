from .models import Blogs,Comments
from rest_framework import serializers


class comments_serializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields=['comments']

class blog_serializer(serializers.ModelSerializer):
    comments=comments_serializer(many=True,read_only=True)
    class Meta:
        model=Blogs
        fields=['id','blog_title','blog_text','comments']
