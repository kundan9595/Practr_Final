# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 17:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_interests'),
    ]

    operations = [
        migrations.CreateModel(
            name='judge_detail',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('degree', models.CharField(default='', max_length=100)),
                ('website', models.EmailField(default='dummy@dummy.com', max_length=254)),
                ('designation', models.CharField(default='', max_length=100)),
                ('industry_exp', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='student_detail',
            fields=[
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('degree', models.CharField(default='', max_length=100)),
                ('college', models.CharField(default='', max_length=150)),
                ('year', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third')], default='First', max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='college',
        ),
        migrations.RemoveField(
            model_name='student',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='student',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='student',
            name='industry_exp',
        ),
        migrations.RemoveField(
            model_name='student',
            name='website',
        ),
        migrations.RemoveField(
            model_name='student',
            name='year',
        ),
        migrations.AlterField(
            model_name='student',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
    ]
