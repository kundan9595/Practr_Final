# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20170329_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.upload_loction),
        ),
    ]
