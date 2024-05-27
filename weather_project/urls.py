from django.urls import path
from weather_api.views import weather_api_view, weather_history_view, delete_weather_view, get_specific_weather_view
from user_api.views import  user_register, user_login, user_update, user_delete, user_info

urlpatterns = [
    # Endpoint for retrieving current weather information
    path('weather/', weather_api_view, name='weather_api'),

    # Endpoint for retrieving a list of weather history records
    path('weather/history/', weather_history_view, name='weather-history-list'),
    
    # Endpoint for retrieving specific weather information by ID
    path('weather/history/<str:weather_id>/', get_specific_weather_view, name='get_specific_weather'),
    
    #
    path('user', user_info, name='user_info'),

    #
    path('user/register/', user_register, name='user_register'),
    
    #
    path('user/login/', user_login, name='user_login'),

    #
    path('user/update/', user_update, name='user_update'),

    #
    path('user/delete', user_delete, name='user_delete'),

]

