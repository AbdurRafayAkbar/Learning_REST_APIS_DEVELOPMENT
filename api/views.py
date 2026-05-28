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


# # LEarning CLASS BASED VIEW
from rest_framework.views import APIView
from employes.models import Employ
from .serializers import EmploySerializer
from django.http import Http404

# class Employs_data(APIView):
#     def get(self,request):
#         employess=Employ.objects.all()
#         serializer=EmploySerializer(employess,many=True)
#         return Response(serializer.data,status=status.HTTP_302_FOUND)
    
#     def post(self,request):
#         serializer=EmploySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# # FOR PRIMARY KEYS VALUES
# class Employs_detail_data(APIView):     
#     def get_object(self,pk):
#         try:
#             return Employ.objects.get(pk=pk)
#         except:
#             raise Http404
#     def get(self,request,pk):
#         employe=self.get_object(pk)
#         serializer=EmploySerializer(employe)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
    
#     def delete(self,request,pk):
#         employe=self.get_object(pk)
#         employe.delete()
#         return Response(status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         employe=self.get_object(pk)
#         serializer=EmploySerializer(employe,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



## UNDERSTANDING MIXINS

from rest_framework import mixins
from rest_framework import generics

class Employs_data(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset =Employ.objects.all()
    serializer_class=EmploySerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    

class Employs_detail_data(mixins.DestroyModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset=Employ.objects.all()
    serializer_class=EmploySerializer

    def get(self,request,pk):
        return self.retrieve(request, pk)
    
    def delete(self,request,pk):
        return self.delete(request, pk)
    
    def put(self,request,pk):
        return self.update(request, pk)