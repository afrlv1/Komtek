from django_filters import rest_framework as filters
from .models import Guide, Element


class GuideFilter(filters.FilterSet):
    date = filters.DateFilter(field_name='date')
    guide = filters.CharFilter(field_name='guide')
    version = filters.CharFilter(field_name='version')

    class Meta:
        model = Guide
        fields = ('date', 'guide', 'version',)


class ElementFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='id')
    guide = filters.CharFilter(field_name='guide')
    code = filters.CharFilter(field_name='code')
    value = filters.CharFilter(field_name='value')

    class Meta:
        model = Element
        fields = ('id', 'guide', 'code', 'value',)
