from django_filters import rest_framework as filters
from .models import Guide, Element


class GuideFilter(filters.FilterSet):
    date = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Guide
        fields = ('date',)


class ElementFilter(filters.FilterSet):
    guide = filters.CharFilter(field_name='guide', lookup_expr='contains')
    version = filters.CharFilter(field_name='guide__version', lookup_expr='contains')

    class Meta:
        model = Element
        fields = ('guide', 'version',)


class ValidateFilter(filters.FilterSet):
    guide = filters.CharFilter(field_name='guide', lookup_expr='contains')
    code = filters.CharFilter(field_name='code', lookup_expr='contains')
    value = filters.CharFilter(field_name='value', lookup_expr='contains')
    date = filters.CharFilter(field_name='guide__date', lookup_expr='contains')
    version = filters.CharFilter(field_name='guide__version', lookup_expr='contains')

    class Meta:
        model = Element
        fields = ('guide', 'version', 'code', 'value')
