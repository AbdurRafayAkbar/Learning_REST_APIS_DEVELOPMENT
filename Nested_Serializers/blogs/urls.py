from django.urls import path
from .views import Blog_presentaion,Comments_presentation,Detailed_Blogs_View,Detailed_Comments_View

urlpatterns = [
    path("blogs/",Blog_presentaion.as_view(),name="blogs_page"),
    path("blogs/<int:pk>/",Detailed_Blogs_View.as_view(),name="detailed_blog_page"),
    path("comments/",Comments_presentation.as_view(),name="comments_page"),
    path("comments/<int:pk>/",Detailed_Comments_View.as_view(),name="detailed_blog_page"),
]
