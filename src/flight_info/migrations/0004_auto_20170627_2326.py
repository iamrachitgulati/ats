# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_info', '0003_auto_20170627_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='operation_days',
            field=models.CharField(max_length=13),
        ),
    ]
