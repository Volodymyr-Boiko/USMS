# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management_system', '0002_remove_userprofile_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstatus',
            name='user_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='management_system.UserProfile'),
        ),
    ]
