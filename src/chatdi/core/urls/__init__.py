from django.urls import include, path

from core.admin import admin

api = [
	path('v1/', include('core.urls.api_v1')),
]

urlpatterns = [
	path('admin/', admin.urls),
	path('api/', include(api)),
]
