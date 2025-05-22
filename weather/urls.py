from django.urls import path
from .views import WeatherRecordView

urlpatterns = [
    path('records/', WeatherRecordView.as_view(), name='weather-records'),
]
