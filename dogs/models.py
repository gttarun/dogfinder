# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    weight = models.IntegerField(default=0)
    longitude = models.FloatField()
    latitude = models.FloatField()
    lastupdated = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name
