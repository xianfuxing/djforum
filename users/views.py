# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserProfileForm, MugshotForm
from .models import User


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class UserProfileChangeView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'users/profile_change.html'
    success_url = '/users/profile'

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)

class MugshotChangeView(LoginRequiredMixin, UpdateView):
    form_class = MugshotForm
    template_name = 'users/mugshot_change.html'
    success_url = '/users/profile'

    def form_valid(self, form):
        if form.has_changed():
            self.request.user.mugshot.delete(save=False)
        return super(MugshotChangeView, self).form_valid(form)

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)