# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-08 17:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0005_auto_20191108_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='lastupdated',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 8, 11, 24, 55, 373394)),
        ),
    ]
