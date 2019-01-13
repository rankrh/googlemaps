# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 18:08:43 2019

@author: Bob
"""

from urllib.request import urlopen
import os
import ssl
import json

BASE_URL = 'https://maps.googleapis.com/'
KEY = os.environ.get('GOOGLE_API_KEY')
ctx = ssl.create_default_context()


def GeoCode(location, output_format='json', language=''):
    location = location.replace(' ', '+')
    
    URL_EXTENSION = 'maps/api/geocode/'
    url = BASE_URL + URL_EXTENSION + output_format
    url += '?address=' + location
    url += '&key=' + KEY
    
    data = json.loads(urlopen(url, context=ctx).read().decode('utf-8'))
    lat = data['results'][0]['geometry']['location']['lat']
    long = data['results'][0]['geometry']['location']['lng']
    return (lat, long)