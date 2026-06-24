from django.urls import path
from .views import Blogs_View,Detailed_Blog_View

urlpatterns = [
    path("blogs/",Blogs_View.as_view(),name="blog_view_page"),
    path("blogs/<int:id>/",Detailed_Blog_View.as_view(),name="detailed_view_page")
]
