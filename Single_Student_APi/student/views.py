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

    def get(self,request):
        return self.retrieve(request)
    
    def put(self,request):
        return self.update(request)
    
    def delete(self,request):
        return self.destroy(request)