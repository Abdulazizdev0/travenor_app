from rest_framework import viewsets
from booking.models import Payment
from .serializers import PaymentSerializer
from ..permissions import IsOwnerOrReadOnly

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Payment.objects.none()
        if self.request.user.is_authenticated:
            return Payment.objects.filter(booking__user=self.request.user)
        return Payment.objects.none()