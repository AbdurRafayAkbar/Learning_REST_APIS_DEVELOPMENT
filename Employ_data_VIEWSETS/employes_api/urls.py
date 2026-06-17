from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employes",views.EmployessViewset,name="Employes Data")

urlpatterns = [
    path("",include(router.urls))
]
