from django.urls import path
from weather_api.views import WeatherAPIView, WeatherHistoryDetailAPIView, WeatherHistoryListAPIView 

urlpatterns = [
    path('weather/', WeatherAPIView.as_view(), name='weather'),
    path('history/', WeatherHistoryListAPIView.as_view(), name='weather-history-list'),
    path('history/<int:pk>/', WeatherHistoryDetailAPIView.as_view(), name='weather-history-detail'),
]

