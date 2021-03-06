# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-22 18:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20161220_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Your email address that will be used to access the platform', max_length=254, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'Type a valid email. This fields should only contain letters, numbers and the characteres: @/./+/-/_ .', 'invalid')], verbose_name='Mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/', validators=[users.models.validate_img_extension], verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='show_email',
            field=models.IntegerField(blank=True, choices=[(1, 'Allow everyone to see my address'), (2, 'Only classmates can see my address'), (3, 'Nobody can see my address')], default=1, null=True, verbose_name='Show email?'),
        ),
    ]
