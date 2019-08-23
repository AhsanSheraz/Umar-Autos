# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-21 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190121_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoiceitems',
            name='partID',
        ),
        migrations.AddField(
            model_name='invoiceitems',
            name='part',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.Part'),
            preserve_default=False,
        ),
    ]