from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.permissions import IsAdminUser

from core.spectacular import schemas


@schemas.privat_schema_view
class PrivateSchemaView(SpectacularAPIView):
	permission_classes = [IsAdminUser]


class PrivateSwaggerView(SpectacularSwaggerView):
	permission_classes = [IsAdminUser]
