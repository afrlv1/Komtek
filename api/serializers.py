from rest_framework import serializers
from .models import Guide, Element


class GuideListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'


class ElementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = '__all__'
