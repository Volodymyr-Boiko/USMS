# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.views.generic import DetailView


from .models import Users


class UserListView(ListView):

    model = Users
    template_name = 'user_list.html'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'users': self.model.objects.all()
        })
        return super(UserListView, self).get_context_data(**kwargs)


class UserDetailView(DetailView):

    model = Users
    template_name = 'user.html'

    def get_queryset(self):
        return self.model.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super(UserDetailView, self).get_context_data(**kwargs)


