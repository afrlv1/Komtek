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
            #Directory.objects.filter(start_date__gte=date)
            queryset_list = Guide.objects.raw('''SELECT * 
                                                        FROM termservice_directory
                                                        WHERE start_date >= %s''', [date])
        else:
            queryset_list = Guide.objects.all()
        return queryset_list


class ElementListView(generics.ListAPIView):
    serializer_class = ElementListSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        dir = query_params.get('dir', None)
        version = query_params.get('version', None)

        if dir is not None and version is None:
            queryset_list = Element.objects.raw('''SELECT id, code, value   
                                                    FROM termservice_item_directory 
                                                    WHERE id_dir_id in 
                                                        (SELECT Max(id) as id
                                                        FROM termservice_directory 
                                                        WHERE short_name = %s
                                                        GROUP BY name)''', [dir])

        elif dir is not None and version is not None:
            queryset_list = Element.objects.raw('''SELECT id, code, value   
                                                    FROM termservice_item_directory 
                                                    WHERE id_dir_id in 
                                                        (SELECT id as id
                                                        FROM termservice_directory 
                                                        WHERE short_name = %s and version = %s)''', [dir, version])

        return queryset_list


class ValidateElementListView(generics.ListAPIView):
    serializer_class = ElementListSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        dir = query_params.get('dir', None)
        version = query_params.get('version', None)
        code = query_params.get('code', None)

        if dir is not None and code is not None and version is None:
            queryset_list = Element.objects.raw('''SELECT id, code, value   
                                                    FROM termservice_item_directory 
                                                    WHERE id_dir_id in 
                                                        (SELECT Max(id) as id
                                                        FROM termservice_directory 
                                                        WHERE short_name = %s
                                                        GROUP BY name) and code = %s''', [dir, code])

        elif dir is not None and code is not None and version is not None:
            queryset_list = Element.objects.raw('''SELECT id, code, value   
                                                    FROM termservice_item_directory 
                                                    WHERE id_dir_id in 
                                                        (SELECT id as id
                                                        FROM termservice_directory 
                                                        WHERE short_name = %s and version = %s) and code = %s''', [dir, version, code])

        if not queryset_list:
            queryset_list = [
                {
                'id': None,
                'code': None,
                'value': None
                }
            ]
        return queryset_list
