from django.urls import path
from .views import Blog_presentaion,Comments_presentation

urlpatterns = [
    path("",Blog_presentaion.as_view(),name="blogs_page"),
    path("comments/",Comments_presentation.as_view(),name="comments_page")
]
