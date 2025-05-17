from rest_framework import viewsets
from travel.models import Review
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .serializers import ReviewSerializer
from ..permissions import IsOwnerOrReadOnly

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Review.objects.none()
        if self.request.user.is_authenticated:
            return Review.objects.filter(user=self.request.user)
        return Review.objects.none()

    @action(detail=False, methods=['get'], permission_classes=[IsOwnerOrReadOnly])
    def top_rated(self, request):
        if getattr(self, 'swagger_fake_view', False):
            return Response([])
        limit = int(request.query_params.get('limit', 10))
        min_rating = int(request.query_params.get('min_rating', 0))
        top_reviews = Review.objects.filter(rating__gte=min_rating).order_by('-rating')[:limit]
        serializer = self.get_serializer(top_reviews, many=True)
        return Response(serializer.data)