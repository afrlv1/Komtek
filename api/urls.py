from django.urls import path
from .views import GuideView, GuideElementView,  ValidateElementView

app_name = 'guides'

urlpatterns = [
	path('guides/', GuideView.as_view()),
	path('elements/', GuideElementView.as_view()),
	path('validate/', ValidateElementView.as_view()),
]
