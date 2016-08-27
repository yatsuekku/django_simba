# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-26 23:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_type',
            name='brand_name',
        ),
        migrations.AddField(
            model_name='car_const',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='car_const',
            name='car_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Type_of_car'),
        ),
        migrations.AlterField(
            model_name='car_model',
            name='type_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Car_brand'),
        ),
        migrations.DeleteModel(
            name='Car_type',
        ),
    ]
