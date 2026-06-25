from rest_framework import serializers
from .models import Employes

class Employ_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Employes
        fields="__all__"
        