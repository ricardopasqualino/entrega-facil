#import das bibliotecas 
import django_filters


#import dos arquivos
from .models import Delivery


class FiltroMorador(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Delivery
        fields = ['morador']
