from django.urls import path
from .views import Employ_views

urlpatterns = [
    path("",Employ_views.as_view(),name="Employ_view")
]
