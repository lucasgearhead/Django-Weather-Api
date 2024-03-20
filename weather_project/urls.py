from django.urls import path
from weather_api.views import weather_api_view, weather_history_view

urlpatterns = [
    # Endpoint for retrieving current weather information
    path('weather/', weather_api_view, name='weather_api'),

    # Endpoint for retrieving a list of weather history records
    path('history/', weather_history_view, name='weather-history-list'),
]

