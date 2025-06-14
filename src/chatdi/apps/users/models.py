from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.users.mangers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(
		_('Email address'),
		blank=True,
		unique=True,
	)
	first_name = models.CharField(
		_('First name'),
		max_length=50,
		blank=True,
	)
	last_name = models.CharField(
		_('Last name'),
		max_length=50,
		blank=True,
	)
	confirmation_sent_at = models.DateTimeField(
		_('Confirmation sent at'),
		blank=True,
		null=True,
		help_text=_('The date and time when the confirmation email was sent.'),
	)
	confirmed_at = models.DateTimeField(
		_('Confirmed at'),
		blank=True,
		null=True,
		help_text=_('The date and time when the user confirmed their email address.'),
	)
	display_name = models.CharField(
		_('Display name'),
		max_length=101,
		blank=True,
		null=True,
		help_text=_('The name that will be displayed in the chat.'),
	)
	is_staff = models.BooleanField(
		_('Staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this admin site.'),
	)
	is_active = models.BooleanField(
		_('Active'),
		default=True,
		help_text=_(
			'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'
		),
	)
	date_joined = models.DateTimeField(
		_('Date joined'),
		default=timezone.now,
	)

	objects = UserManager()

	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('User')
		verbose_name_plural = _('Users')

	def clean(self) -> None:
		super().clean()
		self.email = self.__class__.objects.normalize_email(self.email)

	def get_full_name(self) -> str:
		full_name = f'{self.first_name} {self.last_name}'
		return full_name.strip()

	def get_short_name(self) -> str:
		return self.first_name

	def get_display_name(self) -> str:
		return self.display_name or self.get_full_name()

	@property
	def confirmed(self) -> bool:
		return self.confirmed_at is not None
