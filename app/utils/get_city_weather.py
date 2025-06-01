import requests
from app.weather_constants import weather_codes_description


def city_weather(url: str) -> list:
    '''
        The function for obtaining weather for the coming days and creating a dictionary with data based on the response

    :param url: URL weather forecast
    :return: list of weather data
    '''
    weather_day_data = []
    response = requests.get(url)
    if response.status_code != 200:
        return []
    weather = response.json().get('daily')
    len_days = len(weather.get('time'))
    for i in range(len_days):
        weather_code = weather.get('weathercode')[i]
        weather_data = weather_codes_description.get(weather_code, 'Weather code not found')
        day_data = {
            'date': weather.get('time')[i],
            'max_temp': weather.get('temperature_2m_max')[i],
            'min_temp': weather.get('temperature_2m_min')[i],
            'weathercode': weather_data,
        }
        weather_day_data.append(day_data)
    return weather_day_data