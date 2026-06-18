from django.db import models

class Employees(models.Model):

    department_choices=[
        ("Software Engineering","SE"),
        ("Information Technology","IT"),
        ("Computer Science","CS"),
    ]
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.IntegerField()
    department=models.CharField(max_length=100,default="Software Engineering",choices=department_choices)

    def __str__(self):
        return self.name