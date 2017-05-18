import re
from django.core.validators import RegexValidator, MaxLengthValidator
from django.utils.translation import ugettext_lazy as _


# Custom the regex validator
class MaxUsernameValidator(MaxLengthValidator):
    message = _("用户名最长为10个字符")


class StarUsernameValidator(RegexValidator):
    message = _('Σ(っ°Д°;)っ')

StarUsernameValidator = StarUsernameValidator(r"^[a-zA-Z0-9\u4e00-\u9fa5]+$")
MaxUsernameValidator = MaxUsernameValidator(10)


# Define the validator list to ACCOUNT_USERNAME_VALIDATORS
validator_list = [StarUsernameValidator, MaxUsernameValidator]