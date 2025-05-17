from rest_framework import viewsets
from user.models import Saved
from .serializers import SavedSerializer
from ..permissions import IsOwnerOrReadOnly

class SavedViewSet(viewsets.ModelViewSet):
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Saved.objects.none()
        if self.request.user.is_authenticated:
            return Saved.objects.filter(user=self.request.user)
        return Saved.objects.none()