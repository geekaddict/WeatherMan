from django.shortcuts import render
from .models import City
import requests
# Create your views here.
def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=YOUR_API_KEY'
    weather_data = []
    cities = City.objects.all()
    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather) #add the data for the current city into our list
    context = {'weather_data' : weather_data}
    return render(request,'weatherman/index.html', context)
