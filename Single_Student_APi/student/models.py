from django.db import models

class Degree(models.TextChoices):
    Software="Software Engineering"
    Computer="Computer Science"
    BBA="Business Administration"

class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    age=models.IntegerField()
    Degree_selected=models.CharField(max_length=50,choices=Degree,default=Degree.Software)
    created_at=models.DateTimeField()