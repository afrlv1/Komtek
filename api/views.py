from .models import Guide, Element
from .serializers import GuideListSerializer, ElementListSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ElementFilter, GuideFilter


class GuideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = GuideFilter
    filterset_fields = ('date', 'guide', 'version',)


class ElementViewSet(viewsets. ReadOnlyModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = ElementFilter
    filterset_fields = ('id', 'guide', 'code', 'value',)
