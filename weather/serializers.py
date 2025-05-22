from rest_framework import serializers

class CurrentWeatherSerializer(serializers.Serializer):
    city = serializers.CharField()
    country = serializers.CharField()
    temperature = serializers.FloatField()
    description = serializers.CharField()
    humidity = serializers.IntegerField()

class ForecastSerializer(serializers.Serializer):
    day = serializers.IntegerField()
    temperature = serializers.FloatField()
    description = serializers.CharField()
    humidity = serializers.IntegerField()

class WeatherForecastResponseSerializer(serializers.Serializer):
    city = serializers.CharField()
    country = serializers.CharField()
    forecasts = ForecastSerializer(many=True)

from rest_framework import serializers
from .models import WeatherRecord

class WeatherRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherRecord
        fields = ['id', 'city', 'country', 'temperature', 'description', 'humidity', 'created_at']
        read_only_fields = ['id', 'temperature', 'description', 'humidity', 'created_at']
