# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UserProfile(models.Model):

    user_name = models.CharField(max_length=50, unique=True)


class Usertatus(models.Model):

    status = models.CharField(max_length=50)
    user_profile = models.ForeignKey(UserProfile, default='')
