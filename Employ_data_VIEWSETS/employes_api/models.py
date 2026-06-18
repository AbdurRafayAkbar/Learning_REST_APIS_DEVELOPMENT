from django.db import models

class Employees(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.IntegerField()
    department=models.CharField(max_length=100,default="IT")

    def __str__(self):
        return self.name