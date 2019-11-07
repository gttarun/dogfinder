# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Park

def index(request):
    all_parks = Park.objects.order_by('name')
    output = []
    for park in all_parks:
        output.append([str(park.name), str(park.longitude), str(park.latitude)])
    return HttpResponse(output)

def detail(request, park_name):
    all_parks = Park.objects.order_by('name')
    for park in all_parks:
        if park.name == park_name:
            return HttpResponse([park.latitude, " ", park.longitude])
    return HttpResponse("%s NOT FOUND" %park_name)
