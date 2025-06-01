from django.urls import path
from app import views

urlpatterns = [
    path('', views.home_page_view, name='home_view'),
    path('weather/', views.weather_view, name='weather_view'),
]