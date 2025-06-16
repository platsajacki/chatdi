from typing import Any

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as DRFTokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer as DRFTokenRefreshSerializer

from apps.a12n.api.v1.mixins import UserUUIDInjectionMixin


class TokenObtainPairSerializer(DRFTokenObtainPairSerializer, UserUUIDInjectionMixin):
	access = serializers.CharField(read_only=True)
	refresh = serializers.CharField(read_only=True)
	user_uuid = serializers.UUIDField(read_only=True)

	def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
		data = super().validate(attrs)
		return self.inject_user_uuid(data)


class TokenRefreshSerializer(DRFTokenRefreshSerializer, UserUUIDInjectionMixin):
	access = serializers.CharField(read_only=True)
	user_uuid = serializers.UUIDField(read_only=True)

	def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
		data = super().validate(attrs)
		self.user = self.get_user_from_token(attrs['refresh'])
		return self.inject_user_uuid(data)
