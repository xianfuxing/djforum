from django import forms
from django.core import urlresolvers
from django.core.validators import RegexValidator
from django.utils.html import mark_safe

from allauth.account.forms import (
	LoginForm as AllAuthLoginForm,
	SignupForm as AllAuthSignupForm
)

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from captcha.fields import CaptchaField

from .models import User


class LoginForm(AllAuthLoginForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_action = 'account_login'
		self.helper.form_method = 'post'
		self.helper.layout.append(
			HTML("""
			{% if redirect_field_value %}
             <input type="hidden" name="{{ redirect_field_name }}" value="{{ redirect_field_value }}" />
            {% endif %}
            """))
		self.helper.add_input(Submit('submit', '登录'))