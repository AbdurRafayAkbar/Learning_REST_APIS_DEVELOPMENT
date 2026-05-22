from django.shortcuts import render
from .serializers import StudentSerializer
from students.models import StudentModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
@api_view(["GET","POST"])
def student_list(request):
    if request.method=="GET":
        students=StudentModel.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)