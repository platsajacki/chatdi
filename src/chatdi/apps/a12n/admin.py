from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _

from core.admin import admin_site

from apps.a12n.models import SingIn


@admin_site.register_model(SingIn)
class SingInAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'user',
		'created_at',
	)
	fieldsets = (
		(
			_('Sign In Details'),
			{
				'fields': (
					'id',
					'user',
					'ip_address',
				)
			},
		),
		(
			_('Timestamps'),
			{
				'fields': (
					'created_at',
					'updated_at',
				)
			},
		),
	)
	readonly_fields = (
		'id',
		'user',
		'ip_address',
		'created_at',
		'updated_at',
	)

	def get_queryset(self, request: HttpRequest) -> QuerySet:
		return super().get_queryset(request).select_related('user')
