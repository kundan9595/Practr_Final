# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0068_auto_20170420_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rounds',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
