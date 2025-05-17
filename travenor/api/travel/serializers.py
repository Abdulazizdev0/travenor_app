from rest_framework import serializers
from travel.models import Travels,TravelImage



class TravelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelImage
        fields = ['id', 'travel', 'image', 'is_main']
        read_only_fields = ['travel']



class TravelsSerializer(serializers.ModelSerializer):
    images = TravelImageSerializer(many=True, read_only=True, source='travelimage_set')
    class Meta:
        model = Travels
        fields = ['id', 'name', 'description', 'level', 'region', 'created_at', 'start_date', 'end_date', 'price', 'images']
