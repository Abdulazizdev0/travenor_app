from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet,allNotificationViewSet

router = DefaultRouter()
router.register(r'', NotificationViewSet,basename='notification')
router.register(r'allusersends', allNotificationViewSet,basename='allnotification')


urlpatterns = [
    path('', include(router.urls)),
]