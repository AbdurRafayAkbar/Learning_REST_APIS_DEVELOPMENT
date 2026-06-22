from .models import Blogs,Comments
from rest_framework import serializers
class blog_serializer(serializers.ModelSerializer):
    class Meta:
        model=Blogs
        fields="__all__"


class comments_serializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields="__all__"