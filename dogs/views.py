# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Dog
import math
from decimal import *

def index(request):
    all_dogs = Dog.objects.order_by('name')
    output = []
    for dog in all_dogs:
        output.append([str(dog.name), str(dog.longitude), str(dog.latitude)])
    return HttpResponse(output)

def detail(request, dog_name):
    all_dogs = Dog.objects.all()
    for dog in all_dogs:
        if dog.name == dog_name:
            return HttpResponse([dog.longitude, " ", dog.latitude])
    return HttpResponse("%s NOT FOUND" %dog_name)

def id_detail(request, dog_id):
    dog_id = int(dog_id)
    all_dogs = Dog.objects.all()
    for dog in all_dogs:
        if dog.id == dog_id:
            return HttpResponse([dog.longitude, dog.latitude])
    return HttpResponse("%s NOT FOUND" %dog_id)

def nearby(request):
    output = []
    clon = float(request.GET.get('clon'))
    clat = float(request.GET.get('clat'))
    radius = float(request.GET.get('radius'))
    all_dogs = Dog.objects.all()
    for dog in all_dogs:
        if in_range(clon, clat, float(dog.longitude), float(dog.latitude), radius):
            output.append([str(dog.name)])
    return HttpResponse(output)

def update(request):
    name = request.GET.get('name')
    lon = request.GET.get('lon')
    lat = request.GET.get('lat')
    all_dogs = Dog.objects.all()
    for dog in all_dogs:
        if dog.name == name:
            dog.longitude = lon
            dog.latitude = lat
            try:
                dog.save
                return HttpResponse("SUCCESS")
            except Exception as e:
                return HttpResponse(e)
    return HttpResponse("%s NOT FOUND" %name)

def in_range(clon, clat, lon, lat, r):
    rad = float(0.0175)
    d = (math.acos(math.sin(lat * rad) * math.sin(clat * rad) + math.cos(lat * rad) * math.cos(clat * rad) * math.cos((clon * rad) - (lon * rad))) * r * 1000)
    if (d <= r):
        return True
    else:
        return False