from rest_framework import viewsets
from core.models import Region
from .serializers import RegionSerializer
from rest_framework.permissions import IsAuthenticated



class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [IsAuthenticated]