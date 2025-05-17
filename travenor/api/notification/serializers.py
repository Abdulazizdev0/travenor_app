from rest_framework import serializers
from api.user.serializers import UserSerializer
from notification.models import Notification



class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'