# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-24 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potluck', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potluckitem',
            name='potluckItem_text',
            field=models.CharField(default='I.E. Canopy or 2x Dog Collar(s)', max_length=200),
        ),
        migrations.AlterField(
            model_name='potluckitem',
            name='user_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
