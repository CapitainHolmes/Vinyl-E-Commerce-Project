# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-11 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productsVinyls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLineVinyl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='vinyl_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=40)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=40)),
                ('street_address2', models.CharField(max_length=40)),
                ('county', models.CharField(max_length=40)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='orderlinevinyl',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.vinyl_Order'),
        ),
        migrations.AddField(
            model_name='orderlinevinyl',
            name='vinyl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsVinyls.Vinyl'),
        ),
    ]
