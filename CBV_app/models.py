# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):

    user_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    job = models.ForeignKey('Job', blank=True, null=True)

    def __str__(self):
        return '{} {}. Nickname is {}'.format(
            self.user_name,
            self.second_name,
            self.nick_name
        )


class Job(models.Model):

    job_title = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default='Ukraine')

    def __str__(self):
        return self.job_title
