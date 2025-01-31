from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from django.contrib import messages
# Create your views here.



def first(request):
    return render(request, 'core/first.html')



def home(request):
    city_name= request.POST.get("city")
    API_KEY = '69b2fe85e421e016489084a3b6e8e51b'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

    print(city_name)
    response = requests.get(url)

    if response.status_code == 200:
        data= response.json()
        print(request.GET)   # It is a query dictonary 
        print(data)
        #print(data['main']['temp'])
        dt = data['weather'][0]['description']
        tmp = data['main']['temp']
        humidity = data['main']['humidity']
        min_tmp = data['main']['temp_min']
        max_tmp = data['main']['temp_max']
        
        return render(request,'core/home.html',context={'dt':dt, 'tmp':tmp, 'humidity':humidity, 'min_tmp':min_tmp, 'max_tmp':max_tmp,'city_name':city_name})
    else:
        messages.success(request,f"City/Country i.e, {city_name} not found")
        return render(request,"core/home.html")


