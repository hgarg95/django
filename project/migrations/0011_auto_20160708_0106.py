# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20160707_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratelist',
            name='aluminium',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ratelist',
            name='brass',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ratelist',
            name='copper',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ratelist',
            name='iron',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ratelist',
            name='miscellaneous',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ratelist',
            name='old_batteries',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ratelist',
            name='paper',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ratelist',
            name='plastic',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
