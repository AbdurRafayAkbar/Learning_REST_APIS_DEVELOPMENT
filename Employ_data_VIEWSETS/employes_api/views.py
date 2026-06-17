from django.shortcuts import render
from .models import Employees
from .serializers import EmploySerializer
from rest_framework import viewsets
from rest_framework.response import Response
class EmployessViewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Employees.objects.all()
        serializer=EmploySerializer(queryset,manyy=True)
        return Response(serializer)
