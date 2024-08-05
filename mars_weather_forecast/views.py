from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from requests.exceptions import Timeout
import requests
import json

def getData():
    KEY = settings.SECRET_KEY
    url = f"https://api.nasa.gov/planetary/apod?api_key={KEY}"
    headers = {'Content-Type': 'application/json'}
    try:
      response = requests.get(url, headers=headers, timeout=(3.0, 7.5)).json()
      
      result = {
            'date': response.get('date'),
            'url': response.get('url'),
            'title': response.get('title'),
            'explanation': response.get('explanation')
        } 
    except (requests.exceptions.RequestException, Timeout, ConnectionError):
      result = {
            'date': 'Error',
            'url': 'Error',
            'title': 'Error',
            'explanation': 'Error'
        } 
    return result

def index(request):
  params = {
    'date' : '',
    'url' : '',
    'title' : '', 
    'explanation' : '',
  }
  
  params = getData()
  return render(request, 'mars_weather_forecast/index.html', params)