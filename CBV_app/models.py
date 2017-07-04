# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Users(models.Model):

    user_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField()
