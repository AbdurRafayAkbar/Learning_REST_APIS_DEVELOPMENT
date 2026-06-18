from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employes",views.EmployViewset,basename='employ')

urlpatterns = [
    path("",include(router.urls))
]
