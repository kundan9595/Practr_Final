# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0064_auto_20170418_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='team_size',
            field=models.IntegerField(default=1),
        ),
    ]