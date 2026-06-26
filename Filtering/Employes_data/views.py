from django.shortcuts import render
from .models import Employes
from .serializers import Employ_Serializer
from rest_framework import generics
from .filters import Employ_Filter
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CustomPagination

class Employ_views(generics.ListCreateAPIView):
    queryset=Employes.objects.all()
    serializer_class=Employ_Serializer
    filter_backends= [DjangoFilterBackend]
    filterset_class=Employ_Filter
    pagination_class=CustomPagination