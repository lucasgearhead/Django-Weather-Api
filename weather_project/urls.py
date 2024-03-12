from django.urls import path
from weather_api.views import WeatherAPIView, WeatherHistoryDetailAPIView, WeatherHistoryListAPIView 

urlpatterns = [
    # Endpoint for retrieving current weather information
    path('weather/', WeatherAPIView.as_view(), name='weather'),

    # Endpoint for retrieving a list of weather history records
    path('history/', WeatherHistoryListAPIView.as_view(), name='weather-history-list'),

    # Endpoint for retrieving details of a specific weather history record
    path('history/<int:pk>/', WeatherHistoryDetailAPIView.as_view(), name='weather-history-detail'),
]

