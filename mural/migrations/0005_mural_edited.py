# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-06 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mural', '0004_auto_20170206_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='mural',
            name='edited',
            field=models.BooleanField(default=False, verbose_name='Edited'),
        ),
    ]
