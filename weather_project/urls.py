from django.urls import path
from weather_api.views import weather_api_view, weather_history_view, delete_weather_view,get_specific_weather_view

urlpatterns = [
    # Endpoint for retrieving current weather information
    path('weather/', weather_api_view, name='weather_api'),

    # Endpoint for retrieving specific weather information by ID
    path('weather/<str:weather_id>/', get_specific_weather_view, name='get_specific_weather'),

    # Endpoint for deleting weather information by ID
    path('weather/<str:weather_id>/delete', delete_weather_view, name='delete_weather'), 

    # Endpoint for retrieving a list of weather history records
    path('history/', weather_history_view, name='weather-history-list'),

]

