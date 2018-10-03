from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=your_api_key'
    city = 'New Delhi'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    weather = {
        'city' = city,
        'temperature' = city_weather['main']['temp'],
        'description' = city_weather['weather'][0]['description'],
        'icon' = city_weather['weather'][0]['icon']
    }
    context = {'weather' : weather}
    return render(request,'weatherman/index.html', context)
