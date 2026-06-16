from django.urls import path
from .views import StudentsList,SingleStudentList

urlpatterns = [
    path("students/",StudentsList.as_view()),
    path("students/<int:pk>/",SingleStudentList.as_view())
]
