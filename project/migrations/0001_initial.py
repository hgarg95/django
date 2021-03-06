# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.CharField(max_length=50, null=True)),
                ('count', models.AutoField(primary_key=True, serialize=False)),
                ('email_id', models.EmailField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField(null=True)),
                ('address', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('paper', models.PositiveIntegerField()),
                ('plastic', models.PositiveIntegerField()),
                ('iron', models.PositiveIntegerField()),
                ('aluminium', models.PositiveIntegerField()),
                ('copper', models.PositiveIntegerField()),
                ('brass', models.PositiveIntegerField()),
                ('old_batteries', models.PositiveIntegerField()),
                ('miscellaneous', models.PositiveIntegerField()),
                ('amount_paid', models.FloatField(null=True)),
                ('request_for', models.CharField(max_length=300)),
                ('confirmation', models.BooleanField(default=False)),
                ('date_of_pickup', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RateList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper', models.FloatField(null=True)),
                ('plastic', models.FloatField(null=True)),
                ('copper', models.FloatField(null=True)),
                ('aluminium', models.FloatField(null=True)),
                ('brass', models.FloatField(null=True)),
                ('old_batteries', models.FloatField(null=True)),
                ('iron', models.FloatField(null=True)),
                ('miscellaneous', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('count', models.AutoField(primary_key=True, serialize=False)),
                ('email_id', models.EmailField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField(null=True)),
                ('address1', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('address2', models.CharField(max_length=500)),
                ('address3', models.CharField(max_length=500)),
                ('address4', models.CharField(max_length=500)),
            ],
        ),
    ]
