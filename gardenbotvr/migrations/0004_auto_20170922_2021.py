# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-22 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardenbotvr', '0003_auto_20170920_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinate',
            name='x',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='coordinate',
            name='y',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='coordinate',
            name='z',
            field=models.FloatField(),
        ),
    ]
