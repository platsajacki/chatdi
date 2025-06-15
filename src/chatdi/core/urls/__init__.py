from django.urls import include, path

from core.admin import admin_site

api = [
	path('v1/', include('core.urls.api_v1')),
]

urlpatterns = [
	path('admin/', admin_site.urls),
	path('api/', include(api)),
]
