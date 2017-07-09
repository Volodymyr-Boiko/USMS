# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect

from management_system.models import UserProfile
from management_system.models import Usertatus

from USMS.settings import REDIS_CACHE as redis


def register(request):

    if request.method == 'POST' and request.POST['user_name']:
        user_profile = UserProfile(user_name=request.POST['user_name'])
        user_profile.save()
        Usertatus(user_profile=user_profile).save()
        return redirect(login)

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST' and request.POST['user_name']:
        try:
            UserProfile.objects.get(
                user_name=request.POST['user_name']
            )
        except UserProfile.DoesNotExist:
            return HttpResponse('Unauthorized', status=401)
        redis.setex('user_name', 3600, request.POST['user_name'])
        return redirect(status)

    return render(request, 'login.html')


def status(request):
    user_profile = UserProfile.objects.get(user_name=redis.get('user_name'))
    if request.is_ajax() and request.method == 'POST':
        user_status = Usertatus.objects.get(user_profile=user_profile)
        user_status.status = request.POST['status']
        user_status.save()

        return JsonResponse(
            {
                'status': user_status.status.replace('_', ' '),
                'user_name': user_status.user_profile.user_name
            }
        )

    if redis.get('user_name'):
        user_status = Usertatus.objects.get(user_profile=user_profile)
        context = {}
        context['user_name'] = redis.get('user_name')
        context['status'] = user_status.status
        User = Usertatus.objects.all()
        context['User'] = User

        return render(request, 'status.html', context)
    return HttpResponse('Unauthorized', status=401)


def filter_by_status(request):
    if request.is_ajax() and request.method == 'POST':
        user_status = Usertatus.objects.filter(status=request.POST['status'])
        context = {}
        for item in user_status:
            context.update({item.user_profile.user_name: item.status})
        if context:
            return JsonResponse(context)
        return redirect(status)
