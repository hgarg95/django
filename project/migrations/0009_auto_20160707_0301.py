# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20160707_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='aluminium',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='brass',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='copper',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='iron',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='miscellaneous',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='old_batteries',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='paper',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='plastic',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
