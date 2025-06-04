# apps/weather/serializers.py

from rest_framework import serializers
from .models import WeatherRecord, City, Region, Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')

class RegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Region
        fields = ('id', 'name', 'country')

class CitySerializer(serializers.ModelSerializer):
    region = RegionSerializer(read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'region')

class WeatherRecordSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    city_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = WeatherRecord
        fields = ('id', 'city', 'city_id', 'temperature', 'description', 'humidity', 'created_at')
        read_only_fields = ['id', 'temperature', 'description', 'humidity', 'created_at']
