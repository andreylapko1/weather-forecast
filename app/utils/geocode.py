import requests
from app.utils.generate_url import make_geocode_url


def get_geocode(city_name: str) -> list[str] | None:
    response = requests.get(make_geocode_url(city_name))
    try:
        data = response.json().get('results')[0]
    except TypeError:
        return None
    geo_data = [data.get(a) for a in data if a in ('latitude', 'longitude')]
    if len(geo_data) != 0:
        return geo_data
    else:
        return None