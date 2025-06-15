from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthEventType(models.TextChoices):
	SIGN_IN = 'sign_in', _('Sign In')
	REFRESH = 'refresh', _('Token Refresh')
