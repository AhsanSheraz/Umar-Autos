# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-19 15:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190113_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='part',
            name='date_modified',
        ),
    ]
