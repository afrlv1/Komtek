from rest_framework import routers
from .views import GuideViewSet, ElementViewSet, ValidateViewSet


router = routers.DefaultRouter()
router.register(r'guides', GuideViewSet)
router.register(r'elements', ElementViewSet)
router.register(r'validate', ValidateViewSet)
urlpatterns = router.urls
