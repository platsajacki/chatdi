from typing import Any

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView as DRFTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView as DRFTokenRefreshView

from apps.a12n.api.v1 import schemas
from apps.a12n.api.v1.mixins import LogAuthLogMixin
from apps.a12n.enums import AuthEventType


@schemas.token_obtain_pair_view
class TokenObtainPairView(DRFTokenObtainPairView, LogAuthLogMixin):
	def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
		response = super().post(request, *args, **kwargs)
		self.log_sign_in(requset=request, user_uuid=response.data.get('user_uuid'), event_type=AuthEventType.SIGN_IN)
		return response


@schemas.token_refresh_view
class TokenRefreshView(DRFTokenRefreshView, LogAuthLogMixin):
	def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
		response = super().post(request, *args, **kwargs)
		self.log_sign_in(requset=request, user_uuid=response.data.get('user_uuid'), event_type=AuthEventType.REFRESH)
		return response
