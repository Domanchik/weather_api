from rest_framework import generics
from .models import WeatherRecord, City
from .serializers import WeatherRecordSerializer
import random
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class WeatherRecordView(generics.ListCreateAPIView):
    queryset = WeatherRecord.objects.select_related('city__region__country').all()
    serializer_class = WeatherRecordSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['city__name', 'city__region__name', 'city__region__country__name']
    search_fields = ['description', 'city__name']

    def perform_create(self, serializer):
        """
        Ожидает `city_id` в POST-запросе. Остальные данные генерируются.
        """
        city_id = self.request.data.get('city_id')
        city = get_object_or_404(City, id=city_id)

        temperature = round(random.uniform(15.0, 30.0), 1)
        description = random.choice(["Солнечно", "Облачно", "Дождливо", "Снег"])
        humidity = random.randint(40, 80)

        serializer.save(
            city=city,
            temperature=temperature,
            description=description,
            humidity=humidity
        )
