# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0059_auto_20170417_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='about',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='student',
            name='location',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
