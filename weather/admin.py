# apps/weather/admin.py

from django.contrib import admin
from .models import Country, Region, City, WeatherRecord

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name']
    list_filter = ['country']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']
    search_fields = ['name']
    list_filter = ['region', 'region__country']

@admin.register(WeatherRecord)
class WeatherRecordAdmin(admin.ModelAdmin):
    list_display = ['city', 'temperature', 'description', 'humidity', 'created_at']
    search_fields = ['city__name', 'description']
    list_filter = ['city__region__country', 'created_at']
