# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Dog(models.Model):
	name = models.CharField(max_length=50)
	breed = models.CharField(max_length=50)
	gender = models.CharField(max_length=20)
	color = models.CharField(max_length=20)
	tail = models.CharField(max_length=20)
	fur_type = models.CharField(max_length=20)
	weight = models.IntegerField(default=0)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	lastupdate = models.DateTimeField()

	def __str__(self):
		return self.name
