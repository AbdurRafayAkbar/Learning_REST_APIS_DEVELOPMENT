from django.shortcuts import render
from .models import Employees
from .serializers import EmploySerializer
from rest_framework import viewsets , status
from rest_framework.response import Response
class EmployessViewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Employees.objects.all()
        serializer=EmploySerializer(queryset,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer=EmploySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
