from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'', EmployeeViewSet,basename='travel')

urlpatterns = [
    path('', include(router.urls)),
]