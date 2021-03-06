# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-16 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='order',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_subject', to='subjects.Subject', verbose_name='Subject'),
        ),
    ]
