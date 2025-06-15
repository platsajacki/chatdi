from apps.a12n.api.v1 import schemas
from rest_framework_simplejwt.views import TokenObtainPairView as DRFTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView as DRFTokenRefreshView


@schemas.token_obtain_pair_view
class TokenObtainPairView(DRFTokenObtainPairView): ...


@schemas.token_refresh_view
class TokenRefreshView(DRFTokenRefreshView): ...
