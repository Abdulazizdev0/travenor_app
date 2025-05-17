from rest_framework import serializers
from api.user.serializers import UserSerializer
from user.models import Saved


class SavedSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Saved
        fields = '__all__'