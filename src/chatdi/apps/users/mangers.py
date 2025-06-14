from __future__ import annotations

from typing import TYPE_CHECKING, Any

from django.contrib.auth.models import UserManager as DjangoUserManager

if TYPE_CHECKING:
	from apps.users.models import User


class UserManager(DjangoUserManager):
	def create_user(self, email: str, password: str | None = None, **extra_fields: Any) -> User:
		if not email:
			raise ValueError('Email is required')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email: str, password: str | None = None, **extra_fields: Any) -> User:
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		return self.create_user(email, password, **extra_fields)
