class WeatherEntity:
    def __init__(self, coord_lon, coord_lat, weather_main, weather_description,
                 temp, feels_like, temp_min, temp_max, pressure, humidity,
                 sea_level, grnd_level, visibility, wind_speed, wind_deg,
                 wind_gust, clouds_all, rain_one_hr, rain_three_hr, snow_one_hr,
                 snow_three_hr, date_time, country, city, sunrise, sunset, timezone, cod):
        self.coord_lon = coord_lon
        self.coord_lat = coord_lat
        self.weather_main = weather_main
        self.weather_description = weather_description
        self.temp = temp
        self.feels_like = feels_like
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.pressure = pressure
        self.humidity = humidity
        self.sea_level = sea_level
        self.grnd_level = grnd_level
        self.visibility = visibility
        self.wind_speed = wind_speed
        self.wind_deg = wind_deg
        self.wind_gust = wind_gust
        self.clouds_all = clouds_all
        self.rain_one_hr = rain_one_hr
        self.rain_three_hr = rain_three_hr
        self.snow_one_hr = snow_one_hr
        self.snow_three_hr = snow_three_hr
        self.date_time = date_time
        self.country = country
        self.city = city
        self.sunrise = sunrise
        self.sunset = sunset
        self.timezone = timezone
        self.cod = cod

    def __str__(self):
        return f"Weather in {self.city}: {self.weather_main}, {self.temp}"