from rest_framework import viewsets
from core.models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]