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
@api_view(["GET","PUT","DELETE"])      
def student_detail_view(request,pk):
    try:
        student=StudentModel.objects.get(pk=pk)
        # serializer=StudentSerializer(student)
    except StudentModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=="PUT":
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
