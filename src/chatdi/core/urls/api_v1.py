from django.urls import include, path

from core.spectacular.views import PrivateSchemaView, PrivateSwaggerView

urlpatterns = [
	path('auth/', include('apps.a12n.urls')),
	# path('users/', include('apps.users.urls')),
	path('privat/schema/', PrivateSchemaView.as_view(), name='privat-schema'),
	path(
		'privat/docs/',
		PrivateSwaggerView.as_view(url_name='privat-schema'),
		name='privat-swagger-ui',
	),
]
