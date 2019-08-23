# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-19 15:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190119_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='part',
            name='date_modified',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]