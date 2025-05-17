from rest_framework import viewsets
from travel.models import TravelGuide
from .serializers import TravelGuideSerializer
from ..permissions import IsEmployeeOrReadOnly



class TravelGuideViewSet(viewsets.ModelViewSet):
    queryset = TravelGuide.objects.all()
    serializer_class = TravelGuideSerializer
    permission_classes = [IsEmployeeOrReadOnly]