# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Dog
from .serializers import DogSerializer
import math, json
from datetime import datetime

# return all dogs in database
@csrf_exempt
def index(request):
    if request.method == 'GET':
        serializer = DogSerializer(Dog.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DogSerializer(dog, data=data)
        if serializer.is_valid():
            serializer.data['lastupdated'] = datetime.now()
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400)


# Retrieve, update or delete a dog in database.
@csrf_exempt
def dog_details(request, dog_id):
    
    try:
        dog = Dog.objects.get(pk=dog_id)
    except Dog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DogSerializer(dog)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DogSerializer(dog, data=data)
        if serializer.is_valid():
            serializer.data['lastupdated'] = datetime.now()
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dog.delete()
        return HttpResponse(status=204)

# find all nearby dogs within a radius of a given longitude & latitude
def all_nearby(request):

    try:
        data = json.loads(request.body)
        lon = float(data['lon'])
        lat = float(data['lat'])
        radius = float(data['radius'])
    except:
        return HttpResponse(status=204)

    dogs_nearby = []
    if request.method == 'GET':
        serializer = DogSerializer(Dog.objects.all(), many=True)
        for each in serializer.data:
            if in_range(lon, lat, each['longitude'], each['latitude'], radius):
                dogs_nearby.append(each)
        return JsonResponse(dogs_nearby, status=200, safe=False)

# spherical law of cosines to figure out distance from given coordinates (in radians) within a certain radius (in miles)
def in_range(clon, clat, lon, lat, r):
    rad = float(0.0175) # for radians conversion
    d = (math.acos(math.sin(lat * rad) * math.sin(clat * rad) + math.cos(lat * rad) * math.cos(clat * rad) * math.cos((clon * rad) - (lon * rad))) * r * 1000)
    
    # if d is equal to or less than r, which is the given radius then the lon/lat are within the radius/range
    if (d <= r):
        return True
    else:
        return False