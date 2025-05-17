from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TravelGuideViewSet

router = DefaultRouter()
router.register(r'', TravelGuideViewSet,basename='travel')

urlpatterns = [
    path('', include(router.urls)),
]