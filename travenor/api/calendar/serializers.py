# api/booking/serializers.py
from rest_framework import serializers
from travel.models import Travels
from booking.models import Booking

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travels
        fields = ['id', 'name', 'description', 'level', 'region', 'start_date', 'end_date', 'price']

class CalendarSerializer(serializers.ModelSerializer):
    travel = TravelSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'travel', 'start_date', 'status', 'guests_count', 'created_at']