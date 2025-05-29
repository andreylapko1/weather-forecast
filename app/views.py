from datetime import datetime
from idlelib import history

from django.shortcuts import render, redirect

from app.models import Visitor, VisitorSearch
from app.utils.generate_url import make_weather_url
from app.utils.geocode import get_geocode
from app.utils.get_city_weather import city_weather
from app.utils.track_search import track


def home_page_view(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    visitor, is_created = Visitor.objects.get_or_create(session_key=session_key)
    history = VisitorSearch.objects.filter(visitor=visitor).all()
    if request.method == "POST":
        city = request.POST.get('city')
        track(visitor, city)
        geo_data = get_geocode(city)
        if geo_data is not None:
            lat, lon = geo_data
            weather_url = make_weather_url(lat, lon)
            results = city_weather(weather_url)
            results['time'] = str(datetime.fromisoformat(results['time']))
            request.session['weather'] = results
            return redirect('weather_view')
    return render(request, 'app/home.html', context={'history': history})


def weather_view(request):
    results = request.session.get('weather')
    return render(request, 'app/weather_view.html', context={'weather': results, })

# Create your views here.
