from django.shortcuts import render,get_object_or_404
from .models import Employees
from .serializers import EmploySerializer
from rest_framework import viewsets , status
from rest_framework.response import Response



# class EmployessViewset(viewsets.ViewSet):
#     def list(self,request):
#         queryset=Employees.objects.all()
#         serializer=EmploySerializer(queryset,many=True)
#         return Response(serializer.data)
#     def create(self,request):
#         serializer=EmploySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#     def retrieve(self,request,pk):
#         employe=get_object_or_404(Employees,pk=pk)
#         serializer=EmploySerializer(employe)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def put(self,request,pk):
#         employ=Employees.objects.get(pk=pk)
#         serializer=EmploySerializer(employ,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return serializer.error_messages
#     def destroy(self,request,pk):
#         employ=Employees.objects.get(pk=pk)
#         employ.delete()
#         return Response({
#             "message":"Employ Delterd Successfully"
#         },
#         status=status.HTTP_204_NO_CONTENT)
    
#MODEL VIEW SET

class EmployViewset(viewsets.ModelViewSet):
    queryset=Employees.objects.all()
    serializer_class = EmploySerializer
