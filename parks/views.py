# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Park
import json
from django.core.serializers import serialize

# return all parks
def index(request):
    all_parks = serialize("json", Park.objects.all())
    return HttpResponse(all_parks)

# given the name of park, return details if found
def detail(request, park_name):
    output = {'status': 400, 'response': 'park not in database'}
    all_parks = Park.objects.all()
    for park in all_parks:
        if park.name.lower() == park_name.lower():
            output['status'] = 200
            output['response'] = "SUCCESS"
            output['location'] = str(park.longitude) + ", " + str(park.latitude)
            return HttpResponse(json.dumps(output), content_type='application/json')
    return HttpResponse(json.dumps(output), content_type='application/json')
