# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170819_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
    ]