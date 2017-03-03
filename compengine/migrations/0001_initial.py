# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-02 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.IntegerField()),
                ('load_zone', models.CharField(max_length=256)),
                ('utility_name', models.CharField(max_length=256)),
                ('utility_short_name', models.CharField(max_length=256)),
                ('esco', models.CharField(max_length=256)),
                ('commodity', models.CharField(max_length=256)),
                ('offer_type', models.CharField(max_length=256)),
                ('active', models.BooleanField()),
                ('rate_kwh', models.FloatField()),
                ('green', models.BooleanField()),
                ('minimum_term', models.CharField(max_length=256)),
                ('has_cancellation_fee', models.BooleanField()),
                ('cancellation_fee', models.FloatField()),
                ('dt_created', models.DateTimeField()),
                ('dt_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]