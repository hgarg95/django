# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 20:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20160705_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='password',
        ),
    ]
