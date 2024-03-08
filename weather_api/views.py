from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import WeatherSerializer
from .models import Weather
import requests

class WeatherAPIView(APIView):
    def get(self, request):
        city = request.query_params.get('city', 'Sorocaba')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1871496f2ca4459545804dd8e8be545b"
        response = requests.get(url)
        data = response.json()

        # Save data in the database
        weather_data = Weather.objects.create(
            city=data['name'],
            temperature=data['main']['temp'],
            description=data['weather'][0]['description']
        )

        serializer = WeatherSerializer(weather_data)
        return Response(serializer.data)

