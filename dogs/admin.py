# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Dog
from parks.models import Park

admin.site.register(Dog)
admin.site.register(Park)
