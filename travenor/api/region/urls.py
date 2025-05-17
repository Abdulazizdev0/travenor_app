from django.urls import path, include
from rest_framework import routers
from .views import  RegionViewSet

router = routers.DefaultRouter()
router.register(r'',RegionViewSet,basename='region')

urlpatterns = [
    path('', include(router.urls)),
]