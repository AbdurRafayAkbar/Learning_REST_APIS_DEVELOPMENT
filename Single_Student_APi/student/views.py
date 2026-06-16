from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework import mixins,generics

class Students(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=StudentModel.objects.all()
    serializer_class = StudentSerializer 

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class SingleStudent(mixins.DestroyModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset=StudentModel.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)