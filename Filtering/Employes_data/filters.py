import django_filters
from .models import Employes

class Employ_Filter(django_filters.FilterSet):
    designation=django_filters.CharFilter('designation',lookup_expr="iexact")
    class Meta:
        model=Employes
        fields=["designation"]