from .models import Guide, Element
from .serializers import GuideListSerializer, ElementListSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ElementFilter, GuideFilter, ValidateFilter


#  Получение всех справочников или актуальных на указанную дату
class GuideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = GuideFilter
    filterset_fields = ('date',)


#  Получение элементов заданного справочника текущей версии или указанной версии
class ElementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = ElementFilter
    filterset_fields = ('guide', 'version',)


#  Проверка наличия элементов заданного справочника текущей версии или указанной версии
#  Возвращает null если элемент не найден.
class ValidateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = ValidateFilter
    filterset_fields = ('guide', 'version', 'code', 'value')
