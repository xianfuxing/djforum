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
        

class SignupForm(AllAuthSignupForm):
    captcha = CaptchaField(label='验证码',
                           help_text='如果看不清验证码，请点击图片刷新')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = 'account_signup'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', '注册'))

        self.fields['username'].help_text = '用户名只能包含数字和字母'
        self.fields['password1'].help_text = '不能使用纯数字作为密码，至少8个字符'