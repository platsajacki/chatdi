from django.urls import path

from core.admin import admin

urlpatterns = [
	path('admin/', admin.urls),
]
