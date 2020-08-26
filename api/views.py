from django.shortcuts import render
from rest_framework import generics
from .models import Guide, Element
from .serializers import GuideListSerializer, ElementListSerializer


class GuideListView(generics.ListAPIView):
    serializer_class = GuideListSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        date = query_params.get('date', None)

        if date is not None:
            queryset_list = Guide.objects.filter(start_date__gte=date)
        else:
            queryset_list = Guide.objects.all()
        return queryset_list


class ElementListView(generics.ListAPIView):
    serializer_class = ElementListSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        guide = query_params.get('guide', None)
        version = query_params.get('version', None)

        if guide is not None and version is None:
            queryset_list = Element.objects.filter(guide=guide)
        elif guide is not None and version is not None:
            queryset_list = Element.objects.filter(guide=guide, version=version)
        else:
            queryset_list = Element.objects.all()

        if not queryset_list:
            queryset_list = [{'id': None, 'code': None, 'value': None}]

        return queryset_list


class ValidateElementListView(generics.ListAPIView):
    serializer_class = ElementListSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        guide = query_params.get('guide', None)
        version = query_params.get('version', None)
        code = query_params.get('code', None)

        if guide is not None and code is not None and version is None:
            queryset_list = Element.objects.filter(guide=guide, code=code)

        elif guide is not None and code is not None and version is not None:
            queryset_list = Element.objects.filter(guide=guide, version=version, code=code)

        else:
            queryset_list = Element.objects.all()

        if not queryset_list:
            queryset_list = [{'id': None, 'code': None, 'value': None}]

        return queryset_list
