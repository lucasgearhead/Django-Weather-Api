from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.exceptions import APIException
from .models import Weather
from weather_api.serializers import WeatherSerializer
import requests

class WeatherAPIView(APIView):
    def get(self, request):
        city = request.query_params.get('city', 'nagasaki')
        units = request.query_params.get('units', 'metric')
        appid = request.query_params.get('appid', 'YOUR-APP-ID')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units={units}"
        response = requests.get(url)

        if response.status_code != 200:
            data = response.json()
            error_message = data.get('message', 'Erro ao obter dados do clima.')
            raise APIException(detail=error_message, code=response.status_code)
        
        data = response.json()

        # Salvando os dados no banco de dados
        weather_data = Weather.objects.create(
            coord_lon=data['coord']['lon'],
            coord_lat=data['coord']['lat'],
            weather_main=data['weather'][0]['main'],
            weather_description=data['weather'][0]['description'],
            temp=data['main']['temp'],
            feels_like=data['main']['feels_like'],
            temp_min=data['main']['temp_min'],
            temp_max=data['main']['temp_max'],
            pressure=data['main']['pressure'],
            humidity=data['main']['humidity'],
            sea_level=data['main']['sea_level'] if 'sea_level' in data['main'] else None,
            grnd_level=data['main']['grnd_level'] if 'grnd_level' in data['main'] else None,
            visibility=data['visibility'],
            wind_speed=data['wind']['speed'],
            wind_deg=data['wind']['deg'] if 'deg' in data['wind'] else None,
            wind_gust=data['wind']['gust'] if 'gust' in data['wind'] else None,
            rain_one_hr=data['rain']['1h'] if 'rain' in data and '1h' in data['rain'] else None,
            rain_three_hr=data['rain']['3h'] if 'rain' in data and '3h' in data['rain'] else None,
            snow_one_hr=data['snow']['1h'] if 'snow' in data and '1h' in data['snow'] else None,
            snow_three_hr=data['snow']['3h'] if 'snow' in data and '3h' in data['snow'] else None,
            clouds_all=data['clouds']['all'],
            date_time=data['dt'],
            country=data['sys']['country'],
            sunrise=data['sys']['sunrise'],
            sunset=data['sys']['sunset'],
            timezone=data['timezone'],
            city=data['name'],
            cod=data['cod']
        )


        serializer = WeatherSerializer(weather_data)
        return Response(serializer.data)
    
class WeatherHistoryListAPIView(ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class WeatherHistoryDetailAPIView(RetrieveAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
