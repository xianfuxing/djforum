# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
