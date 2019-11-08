# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Park(models.Model):
    name = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    dog_friendly = models.BooleanField(default=False)
    details = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name
