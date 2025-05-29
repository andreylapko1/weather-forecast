import requests

def city_weather(url: str) -> dict:
    response = requests.get(url)
    weather = response.json().get('current_weather')
    return weather