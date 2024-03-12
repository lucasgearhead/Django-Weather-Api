from django.db import models

class Weather(models.Model):
    """
    Model to store weather data retrieved from an external API.
    """

    # Coordinates
    coord_lon = models.FloatField()  # Longitude
    coord_lat = models.FloatField()  # Latitude

    # Weather information
    weather_main = models.CharField(max_length=50)  # Main weather condition
    weather_description = models.CharField(max_length=50)  # Description of weather condition

    # Temperature
    temp = models.FloatField()  # Temperature in Kelvin, can be converted to °C or °F depending on the 'units' variable
    feels_like = models.FloatField()  # "Feels like" temperature in Kelvin, can be converted to °C or °F depending on the 'units' variable
    temp_min = models.FloatField()  # Minimum temperature in Kelvin, can be converted to °C or °F depending on the 'units' variable
    temp_max = models.FloatField()  # Maximum temperature in Kelvin, can be converted to °C or °F depending on the 'units' variable

    # Atmospheric pressure
    pressure = models.FloatField()  # Atmospheric pressure in hPa

    # Humidity
    humidity = models.FloatField()  # Humidity level in %

    # Additional atmospheric information
    sea_level = models.FloatField(null=True)  # Atmospheric pressure at sea level in hPa
    grnd_level = models.FloatField(null=True)  # Atmospheric pressure at ground level in hPa
    visibility = models.IntegerField()  # Visibility in meters (max 10km)

    # Wind
    wind_speed = models.FloatField()  # Wind speed in m/s
    wind_deg = models.FloatField()  # Wind direction in degrees
    wind_gust = models.FloatField()  # Wind gust speed in m/s

    # Clouds
    clouds_all = models.FloatField()  # Cloudiness in %

    # Precipitation
    rain_one_hr = models.FloatField(null=True)  # Rainfall in the last one hour in mm
    rain_three_hr = models.FloatField(null=True)  # Rainfall in the last three hours in mm
    snow_one_hr = models.FloatField(null=True)  # Snowfall in the last one hour in mm
    snow_three_hr = models.FloatField(null=True)  # Snowfall in the last three hours in mm

    # Date and time
    date_time = models.BigIntegerField()  # Date and time of data retrieval in UNIX timestamp format (UTC)

    # Country and city
    country = models.CharField(max_length=6)  # Country code
    city = models.CharField(max_length=100)  # City name

    # Sunrise and sunset
    sunrise = models.BigIntegerField()  # Sunrise time in UNIX timestamp format (UTC)
    sunset = models.BigIntegerField()  # Sunset time in UNIX timestamp format (UTC)

    # Timezone
    timezone = models.IntegerField()  # Timezone offset in seconds from UTC

    # Response code
    cod = models.IntegerField()  # HTTP response code (200, 400, 404, 500)

    def __str__(self):
        """
        String representation of the Weather object.
        """
        return self.city
