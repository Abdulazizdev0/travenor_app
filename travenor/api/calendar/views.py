from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from booking.models import Booking
from .serializers import CalendarSerializer
from ..permissions import IsOwnerOrReadOnly
from datetime import datetime
from django.db.models import Q
from api.travel.views import CustomPagination
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-created_at')  # Asosiy queryset tartiblangan
    queryset = Booking.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()
        if self.request.user.is_authenticated:
            return Booking.objects.filter(user=self.request.user).order_by('-created_at')  # Tartiblash qo'shildi
        return Booking.objects.all().order_by('-created_at')  # Umumiy queryset ham tartiblangan

    @action(detail=False, methods=['get'], permission_classes=[IsOwnerOrReadOnly])
    def schedule(self, request):
        if getattr(self, 'swagger_fake_view', False):
            return Response({'date': '', 'travel_count': 0, 'travels': []})
        date_str = request.query_params.get('date', None)
        if not date_str:
            return Response({'error': 'Sana kiritilishi shart (YYYY-MM-DD formatida)'}, status=400)

        try:
            selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Sana formati noto‘g‘ri (YYYY-MM-DD bo‘lishi kerak)'}, status=400)

        bookings = self.get_queryset().filter(
            Q(travel__start_date__lte=selected_date) & Q(travel__end_date__gte=selected_date)
        )
        count = bookings.count()
        serializer = self.get_serializer(bookings, many=True)
        return Response({
            'date': date_str,
            'travel_count': count,
            'travels': serializer.data
        })