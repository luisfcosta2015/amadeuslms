# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-10-14 20:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('banco_questoes', '0002_auto_20181001_0204'),
        ('questionary', '0003_auto_20181014_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is correct?')),
                ('order', models.PositiveSmallIntegerField(null=True, verbose_name='Order')),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='useranswer_alternative', to='banco_questoes.Alternative', verbose_name='Answer')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='useranswer_question', to='banco_questoes.Question', verbose_name='Question')),
            ],
        ),
        migrations.CreateModel(
            name='UserQuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ini', models.DateTimeField(auto_now_add=True, verbose_name='Init Date')),
                ('last_update', models.DateTimeField(verbose_name='Last update')),
            ],
        ),
        migrations.AlterField(
            model_name='questionary',
            name='presentation',
            field=models.TextField(blank=True, verbose_name='Presentation'),
        ),
        migrations.AddField(
            model_name='userquest',
            name='questionary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userquest_questionary', to='questionary.Questionary', verbose_name='Questionary'),
        ),
        migrations.AddField(
            model_name='userquest',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userquest_user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='user_quest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='useranswer_userquest', to='questionary.UserQuest', verbose_name='User Questionary'),
        ),
    ]
