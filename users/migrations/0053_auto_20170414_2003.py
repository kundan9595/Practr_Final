# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0052_auto_20170414_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='logo',
            field=models.ImageField(blank=True, default='https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/sq-sample33.jpg', null=True, upload_to=users.models.upload_loction),
        ),
    ]