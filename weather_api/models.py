from django.db import models

class Weather(models.Model):
    coord_lon = models.FloatField()
    coord_lat = models.FloatField()
    weather_main = models.CharField(max_length=50) 
    weather_description = models.CharField(max_length=50) 
    temp = models.FloatField() # K °C °F
    feels_like = models.FloatField() # K °C °F
    temp_min = models.FloatField() # K °C °F 
    temp_max = models.FloatField() # K °C °F
    pressure = models.FloatField() #hPa
    humidity = models.FloatField() #%
    sea_level = models.FloatField(null=True) #Pressão atmosférica ao nível do mar, hPa
    grnd_level = models.FloatField(null=True)  #Pressão atmosférica ao nível do solo, hPa
    visibility = models.IntegerField() #visibilidade em metros (maximo 10km)
    wind_speed = models.FloatField() #m/s
    wind_deg = models.FloatField() #direçao do vento em graus
    wind_gust = models.FloatField() #rajada de vento em m/s
    clouds_all = models.FloatField() #nebulosidade em %
    rain_one_hr = models.FloatField(null=True) #chuva em uma hora em mm
    rain_three_hr = models.FloatField(null=True) #chuva em tres horas em mm
    snow_one_hr = models.FloatField(null=True) #neve em uma hora em mm
    snow_three_hr = models.FloatField(null=True) #neve em tres horas em mm
    date_time = models.BigIntegerField() #UTC
    country = models.CharField(max_length=6) #sigla país
    sunrise = models.BigIntegerField() #UTC
    sunset = models.BigIntegerField() #UTC
    timezone = models.IntegerField() #UTC
    city = models.CharField(max_length=100) 
    cod = models.IntegerField() #retorno 200 400 404 500

    def __str__(self):
        return self.city

