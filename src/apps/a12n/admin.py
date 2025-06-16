from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _

from apps.a12n.models import AuthLog
from core.admin import admin_site


@admin_site.register_model(AuthLog)
class AuthLogAdmin(admin.ModelAdmin):
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
					'event_type',
					'ip_address',
					'user_agent',
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
		'event_type',
		'user_agent',
		'ip_address',
		'created_at',
		'updated_at',
	)

	def get_queryset(self, request: HttpRequest) -> QuerySet:
		return super().get_queryset(request).select_related('user')
