from rest_framework import serializers
from .models import Guide, GuideElement


class GuideSerializer(serializers.ModelSerializer):

	class Meta:
		model = Guide
		fields = ('name', 'title', 'description', 'version', 'date')


class GuideElementSerializer(serializers.ModelSerializer):

	guide = serializers.CharField(source='guide.title', read_only=True)

	class Meta:
		model = GuideElement
		fields = ('guide', 'code', 'value')
