from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
class Employees(models.Model):

    department_choices=[
        ("Software Engineering","SE"),
        ("Information Technology","IT"),
        ("Computer Science","CS"),
    ]
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.IntegerField(validators=[MaxValueValidator(60),MinValueValidator(18)])
    department=models.CharField(max_length=100,default="Software Engineering",choices=department_choices)
    salary=models.IntegerField()

    def __str__(self):
        return self.name