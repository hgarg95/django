# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20160705_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address1',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='address2',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='address3',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='address4',
            field=models.CharField(max_length=500),
        ),
    ]
