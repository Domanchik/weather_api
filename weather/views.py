from rest_framework import generics
from .models import WeatherRecord
from .serializers import WeatherRecordSerializer
import random

class WeatherRecordView(generics.ListCreateAPIView):
    serializer_class = WeatherRecordSerializer

    def get_queryset(self):
        """
        Позволяет фильтровать записи по городу и/или стране.
        Пример:
        http://127.0.0.1:8000/weather/records/?city=Moscow&country=Russia
        """
        queryset = WeatherRecord.objects.all()
        city = self.request.query_params.get('city')
        country = self.request.query_params.get('country')
        if city:
            queryset = queryset.filter(city__iexact=city)
        if country:
            queryset = queryset.filter(country__iexact=country)
        return queryset

    def perform_create(self, serializer):
        """
        При создании записи получает только город и страну (из POST-запроса)
        и генерирует остальные параметры автоматически.
        """
        city = self.request.data.get('city')
        country = self.request.data.get('country')
        
        # Генерация данных "о погоде" — эти значения могут быть получены
        # из реального внешнего сервиса, если потребуется, но здесь они генерируются случайно.
        temperature = round(random.uniform(15.0, 30.0), 1)
        description = random.choice(["Солнечно", "Облачно", "Дождливо", "Снег"])
        humidity = random.randint(40, 80)
        
        serializer.save(
            city=city,
            country=country,
            temperature=temperature,
            description=description,
            humidity=humidity
        )

