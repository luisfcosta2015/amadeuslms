# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-23 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendencies', '0006_auto_20170224_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendencies',
            name='action',
            field=models.CharField(blank=True, choices=[('view', 'Visualize'), ('create', 'Create'), ('answer', 'Answer'), ('access', 'Access'), ('participate', 'Participate'), ('finish', 'Finish'), ('submit', 'Submit')], max_length=100, verbose_name='Action'),
        ),
    ]
