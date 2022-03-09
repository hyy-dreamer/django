from django.shortcuts import render
import requests
from weatherapps.forms import CityForm
from weatherapps.models import City

# Create your views here.
def home(request):
    context={}
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=73f54d6e1dbc534859ecaff80b6ca7e2'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_data=[]
    for city in cities:
        r = requests.get(url.format(city.name)).json()
        city_weather={
            'city' : city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'home.html',context)

