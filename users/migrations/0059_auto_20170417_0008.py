# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0058_auto_20170417_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='logo',
            field=models.ImageField(blank=True, default='default/new_logo', null=True, upload_to=users.models.upload_loction),
        ),
        migrations.AlterField(
            model_name='events',
            name='logo',
            field=models.ImageField(blank=True, default='default/new_logo', null=True, upload_to=users.models.upload_loction),
        ),
    ]
