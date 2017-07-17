# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0002_auto_20170715_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='fare',
            field=models.IntegerField(null=models.IntegerField(null=0)),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='scheduled_arrival',
            field=models.DateField(null='15-07-2017'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='scheduled_departure',
            field=models.DateField(null='14-07-2017'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='weight',
            field=models.IntegerField(null=0),
        ),
    ]