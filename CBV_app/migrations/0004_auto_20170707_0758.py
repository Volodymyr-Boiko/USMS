# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-07 07:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CBV_app', '0003_auto_20170707_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CBV_app.Job'),
        ),
    ]