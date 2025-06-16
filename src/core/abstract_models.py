from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class NameStringMethod(models.Model):
	class Meta:
		abstract = True

	def __str__(self) -> str:
		name = getattr(self, 'name', None)
		if name is not None:
			return str(name)
		return super().__str__()


class TimestampedModel(models.Model):
	created_at = models.DateTimeField(
		_('Created at'),
		auto_now_add=True,
	)
	updated_at = models.DateTimeField(
		_('Updated at'),
		auto_now=True,
	)

	class Meta:
		abstract = True


class UUIDModel(models.Model):
	uuid = models.UUIDField(
		default=uuid4,
		unique=True,
		editable=False,
		db_index=True,
		verbose_name=_('UUID'),
	)

	class Meta:
		abstract = True
