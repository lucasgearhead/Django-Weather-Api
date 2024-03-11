from rest_framework import serializers
from .models import Weather

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['city', 'coord_lon', 'coord_lat', 'weather_main', 'weather_description', 'temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity', 'sea_level', 'grnd_level', 'visibility', 'wind_speed', 'wind_deg', 'wind_gust', 'rain_one_hr', 'rain_three_hr', 'snow_one_hr', 'snow_three_hr', 'clouds_all', 'date_time', 'country', 'sunrise', 'sunset', 'timezone', 'cod']
