from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TravelsViewSet,TravelImageViewSet

router = DefaultRouter()
router.register(r'', TravelsViewSet,basename='travel'),
router.register(r'travel-images', TravelImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
