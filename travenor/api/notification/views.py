from rest_framework import viewsets
from notification.models import Notification
from .serializers import NotificationSerializer
from ..permissions import IsOwnerOrReadOnly,IsAdminOrReadOnly
from user.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Notification.objects.none()
        if self.request.user.is_authenticated:
            return Notification.objects.filter(user=self.request.user)
        return Notification.objects.none()








class allNotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Notification.objects.none()
        if self.request.user.is_authenticated:
            return Notification.objects.filter(user=self.request.user).order_by('-created_at')
        return Notification.objects.none()

    @action(detail=False, methods=['post'], permission_classes=[IsAdminOrReadOnly])
    def send_to_all(self, request):
        """
        Barcha foydalanuvchilarga bildirishnoma yuboradi.
        So'rov tanasi:
        {
            "title": "Bildirishnoma sarlavhasi",
            "message": "Bildirishnoma matni"
        }
        """
        if getattr(self, 'swagger_fake_view', False):
            return Response({'status': 'success'})

        title = request.data.get('title')
        message = request.data.get('message')

        if not title or not message:
            return Response(
                {'error': 'title va message maydonlari kiritilishi shart'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Barcha foydalanuvchilarni olish
        users = User.objects.all()
        if not users.exists():
            return Response(
                {'error': 'Foydalanuvchilar topilmadi'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Har bir foydalanuvchi uchun bildirishnoma yaratish
        notifications = [
            Notification(user=user, title=title, message=message)
            for user in users
        ]
        Notification.objects.bulk_create(notifications)

        return Response(
            {'status': f'{users.count()} ta foydalanuvchiga bildirishnoma yuborildi'},
            status=status.HTTP_201_CREATED
        )