# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User
from .models import Job


# class JobInline(admin.StackedInline):
#     model = Job
#     extra = 3


class UserAdmin(admin.ModelAdmin):

    # fields = ['user_name', 'second_name', 'nick_name', 'age']

    fieldsets = [
        ('Name', {'fields': ['user_name']}),
        ('User information', {'fields': ['nick_name', 'age']}),
    ]

    # inlines = [JobInline]


admin.site.register(User, UserAdmin)


class UserInline(admin.StackedInline):

    model = User
    extra = 1


class JobAdmin(admin.ModelAdmin):

    fieldsets = [
        ('job information', {'fields': ['job_title', 'city']})
    ]

    inlines = [UserInline]


admin.site.register(Job, JobAdmin)
