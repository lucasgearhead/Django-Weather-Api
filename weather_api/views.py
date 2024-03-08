from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Weather
from weather_api.serializers import WeatherSerializer
import requests

class WeatherAPIView(APIView):
    def get(self, request):
        city = request.query_params.get('city', 'Sorocaba')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1871496f2ca4459545804dd8e8be545b"
        response = requests.get(url)
        data = response.json()

        # Salvando o JSON completo no banco de dados
        weather_data = Weather.objects.create(
            city=city,
            json_data=data  # Salvando o JSON completo
        )

        serializer = WeatherSerializer(weather_data)
        return Response(serializer.data)
