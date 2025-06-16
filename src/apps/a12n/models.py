from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.a12n.enums import AuthEventType
from apps.users.models import User
from core.abstract_models import TimestampedModel


class AuthLog(TimestampedModel):
	user = models.ForeignKey(
		User,
		on_delete=models.PROTECT,
		related_name='sign_ins',
		verbose_name=_('User'),
	)
	ip_address = models.GenericIPAddressField(
		verbose_name=_('IP Address'),
		null=True,
		blank=True,
	)
	user_agent = models.TextField(
		verbose_name=_('User Agent'),
		null=True,
		blank=True,
		help_text=_('Browser or client device information at sign in.'),
	)
	event_type = models.CharField(
		max_length=20,
		choices=AuthEventType.choices,
		default=AuthEventType.SIGN_IN,
		verbose_name=_('Event Type'),
		help_text=_('Type of authentication event.'),
	)

	class Meta:
		verbose_name = _('Auth Log')
		verbose_name_plural = _('Auth Logs')
		ordering = ('-created_at',)

	def __str__(self) -> str:
		return f'Auth Log ({self.get_event_type_display()}): {self.user_id} at {self.created_at}'
