from rest_framework import serializers
from .models import AirQualityReading

class AirQualityReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirQualityReading
        fields = '__all__'