from django.db import models

class Degree(models.TextChoices):
    Software_Engineering="Software_Engineering"
    Computer_scince="Computer_Science"
    BBA="Business_Administration"

class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    age=models.IntegerField()
    Degree_selected=models.CharField(max_length=50,choices=Degree,default=Degree.Software_Engineering)
    created_at=models.DateTimeField()