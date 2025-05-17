from rest_framework import serializers
from api.user.serializers import UserSerializer
from booking.models import Booking



class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'