# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserProfileForm
from .models import User


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class UserProfileChangeView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'users/profile_change.html'
    success_url = '/users/profile'

    def get_object(self, queryset=None):
        return self.request.user
