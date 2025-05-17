from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

router = DefaultRouter()
router.register(r'', BookingViewSet,basename='travel')

urlpatterns = [
    path('', include(router.urls)),
]