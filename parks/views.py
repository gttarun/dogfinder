# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Park
from .serializers import ParkSerializer

# return all parks in database
@csrf_exempt
def index(request):
    if request.method == 'GET':
        serializer = ParkSerializer(Park.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ParkSerializer(park, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400)


# Retrieve, update or delete a park in database
@csrf_exempt
def park_details(request, park_name):
    try:
        park = Park.objects.get(name=park_name)
    except Park.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ParkSerializer(park)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ParkSerializer(park, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        park.delete()
        return HttpResponse(status=204)
