from django.urls import path
from . import views

urlpatterns = [
    path('guides/', views.GuideListView.as_view()),
    path('elements/', views.ElementListView.as_view()),
    path('validate/', views.ValidateElementListView.as_view()),
]
