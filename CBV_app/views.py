# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sqlite3 import IntegrityError

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy


from .forms import UserForm
from .models import User


class UserListView(ListView):

    model = User
    template_name = 'user_list.html'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'User': self.model.objects.all()
        })
        return super(UserListView, self).get_context_data(**kwargs)


class UserDetailView(DetailView):

    model = User
    template_name = 'user.html'

    def get_queryset(self):
        return self.model.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super(UserDetailView, self).get_context_data(**kwargs)


class CreateUser(FormView):

    model = User
    form_class = UserForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('User')

    def form_valid(self, form):
        model = self.model(**form.cleaned_data)
        try:
            model.save()
        except:
            return self.form_invalid(form)
        return super(CreateUser, self).form_valid(form)
