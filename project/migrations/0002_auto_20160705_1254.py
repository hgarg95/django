# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='count',
        ),
        migrations.AlterField(
            model_name='user',
            name='email_id',
            field=models.EmailField(max_length=50, primary_key=True, serialize=False),
        ),
    ]