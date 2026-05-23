from rest_framework import serializers
from students.models import StudentModel
from employes.models import Employ
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields="__all__"
class EmploySerializer(serializers.ModelSerializer):
    class Meta:
        model=Employ
        fields="__all__"