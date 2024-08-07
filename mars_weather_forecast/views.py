from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from requests.exceptions import Timeout
import requests
import json

def getData():
    KEY = settings.API_KEY
    url = f"https://api.nasa.gov/planetary/apod?api_key={KEY}"
    headers = {'Content-Type': 'application/json'}
    try:
      response = requests.get(url, headers=headers, timeout=(3.0, 7.5)).json()
      
      result = {
            'date': response.get('date'),
            'url': response.get('url'),
            'title': response.get('title'),
            'explanation': response.get('explanation'),
            'media_type' : response.get('media_type'),
            'copyright' : response.get('copyright'),
        }
    except (requests.exceptions.RequestException, Timeout, ConnectionError):
      result = {
            'date': 'Error',
            'url': '',
            'title': 'Error',
            'explanation': 'Error',
            'media_type' : '',
            'copyright' : '',
        } 
    return result

def index(request):
  params = {
    'date' : '',
    'url' : '',
    'title' : '', 
    'explanation' : '',
    'media_type' : '',
    'copyright' : '',
  }
  
  params = getData()
  return render(request, 'mars_weather_forecast/index.html', params)