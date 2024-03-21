from django.shortcuts import render
from django.http import JsonResponse
from .serializers import WeatherSerializer, WeatherHistorySerializer
from .repositories import WeatherRepository
import requests

def weather_api_view(request):
    if request.method == 'GET':
        # Get query parameters from the request
        city = request.GET.get('city')
        units = request.GET.get('units')
        appid = request.GET.get('appid')

        # Make a request to the OpenWeatherMap API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={appid}"
        response = requests.get(url)

        # Handle non-200 status codes
        if response.status_code != 200:
            data = response.json()
            error_message = data.get('message', 'Erro ao obter dados do clima.')
            return JsonResponse({'error': error_message}, status=response.status_code)

        # Extract data from the response
        data = response.json()

        # Create Weather object using the repository
        weather_repo = WeatherRepository()
        weather_id = weather_repo.create_weather({
            'coord_lon': data['coord']['lon'],
            'coord_lat': data['coord']['lat'],
            'weather_main': data['weather'][0]['main'],
            'weather_description': data['weather'][0]['description'],
            'temp': f"{data['main']['temp']} °C" if units == 'metric' else f"{data['main']['temp']} °F" if units == 'imperial' else f"{data['main']['temp']} K",
            'feels_like': f"{data['main']['feels_like']} °C" if units == 'metric' else f"{data['main']['temp']} °F" if units == 'imperial' else f"{data['main']['temp']} K",
            'temp_min': f"{data['main']['temp_min']} °C" if units == 'metric' else f"{data['main']['temp']} °F" if units == 'imperial' else f"{data['main']['temp']} K",
            'temp_max': f"{data['main']['temp_max']} °C" if units == 'metric' else f"{data['main']['temp']} °F" if units == 'imperial' else f"{data['main']['temp']} K",
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'sea_level': data['main']['sea_level'] if 'sea_level' in data['main'] else None,
            'grnd_level': data['main']['grnd_level'] if 'grnd_level' in data['main'] else None,
            'visibility': data['visibility'],
            'wind_speed': data['wind']['speed'],
            'wind_deg': data['wind']['deg'] if 'deg' in data['wind'] else None,
            'wind_gust': data['wind']['gust'] if 'gust' in data['wind'] else None,
            'rain_one_hr': data['rain']['1h'] if 'rain' in data and '1h' in data['rain'] else None,
            'rain_three_hr': data['rain']['3h'] if 'rain' in data and '3h' in data['rain'] else None,
            'snow_one_hr': data['snow']['1h'] if 'snow' in data and '1h' in data['snow'] else None,
            'snow_three_hr': data['snow']['3h'] if 'snow' in data and '3h' in data['snow'] else None,
            'clouds_all': data['clouds']['all'],
            'date_time': data['dt'],
            'country': data['sys']['country'],
            'sunrise': data['sys']['sunrise'],
            'sunset': data['sys']['sunset'],
            'timezone': data['timezone'],
            'city': data['name'],
            'cod': data['cod']
        })

        # Get the created Weather object from the repository
        weather_data = weather_repo.get_weather(weather_id)

        serializer = WeatherSerializer(weather_data)
        serialized_data = serializer.data_to_dict()

        # Render the template with the weather data as context
        return render(request, 'weather/weather_template.html', serialized_data)

    # Handle other HTTP methods
    return JsonResponse({'error': 'Método não permitido'}, status=405)

def weather_history_view(request):
    if request.method == 'GET':
        # Get all weather data from the repository
        weather_repo = WeatherRepository()
        weather_history = weather_repo.get_all_weather()

        # Serialize the weather history
        weather_history_serializer = WeatherHistorySerializer(weather_history)
        serialized_data = weather_history_serializer.data_to_list()

        # Render the template with the weather history as context
        return render(request, 'weather/weather_history_template.html', {'weather_history': serialized_data})

    # Handle other HTTP methods
    return JsonResponse({'error': 'Método não permitido'}, status=405)
