# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Dog

def index(request):
    all_dogs = Dog.objects.order_by('name')
    output = []
    for dog in all_dogs:
        output.append([str(dog.name), str(dog.latitude), ", ", str(dog.longitude)])
    return HttpResponse(output)

def detail(request, dog_name):
    all_dogs = Dog.objects.all()
    for dog in all_dogs:
        if dog.name == dog_name:
            return HttpResponse([dog.latitude, " ", dog.longitude])
    return HttpResponse("%s NOT FOUND" %dog_name)

def id_detail(request, dog_id):
    all_dogs = Dog.objects.all()
    for dog in all_dogs:
        if dog.id == dog_id:
            return HttpResponse([dog.latitude, dog.longitude])
    return HttpResponse("%s NOT FOUND" %dog_id)
