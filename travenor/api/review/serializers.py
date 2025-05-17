from rest_framework import serializers
from api.user.serializers import UserSerializer
from  travel.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'