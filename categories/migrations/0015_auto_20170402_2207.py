# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-03 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0014_auto_20170224_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='description'),
        ),
    ]
