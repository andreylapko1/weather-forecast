
def make_geocode_url(city_name: str) -> str:
    '''
        Make url to geocode given city name

    :param city_name: string
    :return: string
    '''

    return f'https://geocoding-api.open-meteo.com/v1/search?name={city_name}'


def make_weather_url(latitude: str, longitude: str) -> str:
    '''
        Make url to get weather from given latitude and longitude

    :param city_name: string
    :return: string
    '''

    return f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode&timezone=auto'