from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Guide, GuideElement
from .serializers import GuideSerializer, GuideElementSerializer
from datetime import datetime
from rest_framework.pagination import PageNumberPagination
from .utils import PaginateMixin, ValidateData


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class GuideView(PaginateMixin, APIView):
    pagination_class = BasicPagination
    serializer_class = GuideSerializer

    def get(self, request):
        in_date = request.GET.get('date')
        if in_date:
            try:
                in_date = datetime.strptime(in_date, '%Y-%m-%d')
            except:
                return Response({'Введите корректный формат даты. YYYY-MM-DD'})

            guide = Guide.objects.exclude(date__lte=in_date)
            if guide:
                return self.paginate_run(obj=schedules)

            return Response({f"Guides does not exist on '{in_date}' " })

        guide = Guide.objects.all()
        return self.paginate_run(obj=guide)


class GuideElementView(PaginateMixin, APIView):
    pagination_class = BasicPagination
    serializer_class = GuideElementSerializer

    def get(self, request):
        in_guide = request.GET.get('guide')
        in_version = request.GET.get('version', '')
        if not in_guide:
            content = {"guide": ["This field may not be blank."]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        if in_version:
            try:
                item = Guide.objects.get(version=in_version)
            except Guide.DoesNotExist:
                return Response({'Version does not exist'})

            elements = GuideElement.objects.filter(guide=item)
            return self.paginate_run(obj=guideelements)
        try:
            item = Guide.objects.filter(title=in_guide).order_by('-version').first()
        except Guide.DoesNotExist:
            return Response({'Guide does not exist'})

        elements = GuideElement.objects.filter(guide=item)
        return self.paginate_run(obj=elements)


class ValidateElementView(APIView, ValidateData):
    def get(self, request):
        in_version = request.GET.get('version')
        in_guide = request.GET.get('guide')
        in_code = request.GET.get('code')
        in_value = request.GET.get('value')

        if not in_guide:
            content = {"guide": ["This field may not be blank."]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        item = Guide.objects.filter(title=in_guide)
        if not item:
            content = {f'{in_guide} does not exist'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        if not in_version:
            item = Guide.objects.filter(title=in_guide).order_by('-version').first()
            return self.validate_element(in_code, in_value)
        try:
            item = Guide.objects.get(title=in_guide, version=in_version)
        except Guide.DoesNotExist:
			content = {f'{in_guide} does not exist'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return self.validate_element(in_code, in_value, item)

    def validate_element(self, in_code, in_value, item):
        if not in_code:
            content = {"code": ["This field may not be blank."]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        if not in_value:
            content = {"value": ["This field may not be blank."]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        try:
            element = GuideElement.objects.get(code=in_code, schedule=item)
        except GuideElement.DoesNotExist:
            content = {f'{in_code} does not exist'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        if element.value != in_value:
            content = {f'{in_value} does not equal {element.value}'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"all checked!!!"})