# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-05 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThreeD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='gardenbotvr/models')),
                ('thumb', models.FileField(upload_to='gardenbotvr/thumbs')),
                ('uploaded', models.DateTimeField()),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('PLT', 'Plant'), ('FWR', 'Flower'), ('OTR', 'Other')], max_length=30)),
            ],
        ),
    ]
