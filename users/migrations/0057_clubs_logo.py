# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0056_auto_20170415_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubs',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.upload_loction),
        ),
    ]
