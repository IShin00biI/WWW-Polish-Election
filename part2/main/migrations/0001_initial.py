# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=32)),
                ('area', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('subareas', models.IntegerField()),
                ('people', models.IntegerField()),
                ('cards', models.IntegerField()),
                ('invalid', models.IntegerField()),
                ('grabowski', models.IntegerField()),
                ('ikonowicz', models.IntegerField()),
                ('kalinowski', models.IntegerField()),
                ('korwin', models.IntegerField()),
                ('krzaklewski', models.IntegerField()),
                ('kwasniewski', models.IntegerField()),
                ('lepper', models.IntegerField()),
                ('lopuszanski', models.IntegerField()),
                ('olechowski', models.IntegerField()),
                ('pawlowski', models.IntegerField()),
                ('walesa', models.IntegerField()),
                ('wilecki', models.IntegerField()),
            ],
        ),
    ]