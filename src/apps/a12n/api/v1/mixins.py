from typing import Any

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, Token

from apps.a12n.enums import AuthEventType
from apps.a12n.models import AuthLog
from apps.users.models import User


class UserUUIDInjectionMixin:
	def validate_authenticated_user(self) -> User:
		if not hasattr(self, 'user') or not isinstance(self.user, User):
			raise serializers.ValidationError('User not authenticated.')
		return self.user

	def inject_user_uuid(self, data: dict[str, Any]) -> dict[str, Any]:
		user = self.validate_authenticated_user()
		data['user_uuid'] = str(user.uuid)
		return data

	def get_user_from_token(self, token: Token | None) -> User:
		token = RefreshToken(token)
		user_id = token['user_id']
		user = User.objects.get(id=user_id)
		return user


class LogAuthLogMixin:
	def log_sign_in(self, requset: Response, user_uuid: str, event_type: AuthEventType) -> None:
		if not user_uuid:
			raise ValueError('User UUID is required for logging sign-in events.')
		user = User.objects.get(uuid=user_uuid)
		AuthLog.objects.create(
			user=user,
			event_type=event_type,
			ip_address=requset.META.get('REMOTE_ADDR'),
			user_agent=requset.META.get('HTTP_USER_AGENT', ''),
		)
