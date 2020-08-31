from django.urls import path
from rest_framework import routers
from .views import GuideViewSet, ElementViewSet


router = routers.DefaultRouter()
router.register(r'guides', GuideViewSet)
router.register(r'validate', ElementViewSet)

urlpatterns = router.urls
