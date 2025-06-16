from django.urls import path

from apps.a12n.api.v1.views.jwt import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
