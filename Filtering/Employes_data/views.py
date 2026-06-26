from django.shortcuts import render
from .models import Employes
from .serializers import Employ_Serializer
from rest_framework import generics

class Employ_views(generics.ListCreateAPIView):
    queryset=Employes.objects.all()
    serializer_class=Employ_Serializer
    filterset_fields=["designation",'salary']