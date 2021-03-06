# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20170331_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='interests',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('marketing', models.BooleanField(default=False)),
                ('finance', models.BooleanField(default=False)),
                ('public_relations', models.BooleanField(default=False)),
                ('human_resources', models.BooleanField(default=False)),
                ('ent_dev', models.BooleanField(default=False)),
                ('business_quiz', models.BooleanField(default=False)),
            ],
        ),
    ]
