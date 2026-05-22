from django.shortcuts import render
from .serializers import StudentSerializer
from students.models import StudentModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
@api_view["GET"]
def student_list(request):
    students=StudentModel.objects.all()
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)