# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Park(models.Model):
	name = models.CharField(max_length=50)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	dog_friendly = models.BooleanField(default=False)
	details = models.CharField(max_length=250, null=True)


	def __str__(self):
		return self.name
