from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from travel.models import Travels,TravelImage
from .serializers import TravelsSerializer,TravelImageSerializer
from ..permissions import IsEmployeeOrReadOnly


class CustomPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100


class TravelsViewSet(viewsets.ModelViewSet):
    queryset = Travels.objects.all()
    serializer_class = TravelsSerializer
    permission_classes = [IsEmployeeOrReadOnly]

    def get_queryset(self):
        return Travels.objects.all().order_by('-created_at')


    @action(detail=True, methods=['post'], permission_classes=[IsEmployeeOrReadOnly])
    def upload_image(self, request, pk=None):
        travel = self.get_object()
        serializer = TravelImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(travel=travel)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class TravelImageViewSet(viewsets.ModelViewSet):
    queryset = TravelImage.objects.all()
    serializer_class = TravelImageSerializer
    permission_classes = [IsEmployeeOrReadOnly]

    def get_queryset(self):
        return TravelImage.objects.all()

    def perform_create(self, serializer):
        travel_id = self.request.data.get('travel')
        if not travel_id:
            return Response({'error': 'Travel ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            travel = Travels.objects.get(id=travel_id)
            serializer.save(travel=travel)
        except Travels.DoesNotExist:
            return Response({'error': 'Travel not found'}, status=status.HTTP_404_NOT_FOUND)



