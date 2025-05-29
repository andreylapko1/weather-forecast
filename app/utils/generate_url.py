
def make_geocode_url(city_name: str) -> str:
    return f'https://geocoding-api.open-meteo.com/v1/search?name={city_name}'


def make_weather_url(latitude: str, longitude: str) -> str:
    return f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&timezone=auto'