from django.urls import path
from .views import SingleStudent,Students

urlpatterns = [
    path("students/",Students.as_view(),name='students_Data'),
    path("students/<int:pk>",SingleStudent.as_view(),name="Single_student_details")
    
]
