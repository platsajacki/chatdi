from django.db import models
from django.utils.translation import gettext_lazy as _

from core.abstract_models import TimestampedModel

from apps.users.models import User


class SingIn(TimestampedModel):
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

	class Meta:
		verbose_name = _('Sign In')
		verbose_name_plural = _('Sign Ins')
		ordering = ('-created_at',)

	def __str__(self) -> str:
		return f'Sign In: {self.user_id} at {self.created_at}'
