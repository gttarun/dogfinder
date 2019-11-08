# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Dog
import math, json
from datetime import datetime
from decimal import *

# return all dogs in database
def index(request):
    all_dogs = serialize("json", Dog.objects.all())
    return HttpResponse(all_dogs)

# given dog_id, return coordinates
def detail(request, dog_id):
    dog_id = int(dog_id)
    output = {'status': 400, 'response': 'dog not in database'}
    
    all_dogs = Dog.objects.all()
    for dog in all_dogs:
        if dog.id == dog_id:
            output['status'] = 200
            output['response'] = "SUCCESS"
            output['location'] = [str(dog.longitude), str(dog.latitude)]
            return HttpResponse(json.dumps(output), content_type='application/json')
    return HttpResponse(json.dumps(output), content_type='application/json')

# find all nearby dogs within a radius of a given longitude & latitude
def all_nearby(request):
    output = {'status': 400, 'response': 'no dog(s) within distance', 'in_range': {}}
    clon = float(request.GET.get('clon'))
    clat = float(request.GET.get('clat'))
    radius = float(request.GET.get('radius'))
    all_dogs = Dog.objects.all()
    for dog in all_dogs:
        if in_range(clon, clat, dog.longitude, dog.latitude, radius):
            output['status'] = 200
            output['response'] = "SUCCESS"
            output['in_range'][dog.name] = [str(dog.longitude), str(dog.latitude)]
    return HttpResponse(json.dumps(output), content_type='application/json')

# update location for a given dog (& timestamp when updated)
def update(request):
    output = {'status': 400, 'response': 'could NOT be updated'}
    name = request.GET.get('name')
    lon = request.GET.get('lon')
    lat = request.GET.get('lat')
    all_dogs = Dog.objects.all()
    for dog in all_dogs:
        if dog.name == name:
            dog.longitude = lon
            dog.latitude = lat
            dog.lastupdated = datetime.now()
            try:
                dog.save()
                output['status'] = 200
                output['response'] = 'SUCCESS'
                return HttpResponse(json.dumps(output), content_type='application/json')
            except Exception as e:
                output['details'] = str(e)
                return HttpResponse(json.dumps(output), content_type='application/json')
    return HttpResponse(json.dumps(output), content_type='application/json')

# spherical law of cosines to figure out distance from given coordinates (in radians) within a certain radius (in miles)
def in_range(clon, clat, lon, lat, r):
    rad = float(0.0175) # for radians conversion
    d = (math.acos(math.sin(lat * rad) * math.sin(clat * rad) + math.cos(lat * rad) * math.cos(clat * rad) * math.cos((clon * rad) - (lon * rad))) * r * 1000)
    
    # if d is equal to or less than r, which is the given radius then the lon/lat are within the radius/range
    if (d <= r):
        return True
    else:
        return False