from django.contrib import admin
from django.utils.translation import gettext_lazy as _


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
