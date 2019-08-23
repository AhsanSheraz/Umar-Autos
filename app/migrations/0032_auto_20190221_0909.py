# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-21 04:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20190221_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='labourTotal',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='partTotal',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='taxAmount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='totalAmount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
