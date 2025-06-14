from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from apps.users.models import User
from core.admin import admin

admin.register(Group, GroupAdmin)


@admin.register_model(User)
class UserAdmin(DjangoUserAdmin):
	fieldsets = (
		(
			_('Authentication'),
			{
				'fields': (
					'email',
					'password',
				),
			},
		),
		(
			_('Personal info'),
			{
				'fields': (
					'first_name',
					'last_name',
					'display_name',
				),
			},
		),
		(
			_('Permissions'),
			{
				'fields': (
					'is_active',
					'is_staff',
					'is_superuser',
					'groups',
					'user_permissions',
				),
			},
		),
		(
			_('Important dates'),
			{
				'fields': (
					'last_login',
					'date_joined',
					'confirmation_sent_at',
					'confirmed_at',
				),
			},
		),
	)
	add_fieldsets = (
		(
			None,
			{
				'classes': ('wide',),
				'fields': (
					'email',
					'usable_password',
					'password1',
					'password2',
				),
			},
		),
	)
	list_display = (
		'email',
		'first_name',
		'last_name',
		'is_staff',
	)
	list_filter = (
		'is_staff',
		'is_superuser',
		'is_active',
		'groups',
	)
	search_fields = (
		'first_name',
		'last_name',
		'email',
	)
	ordering = ('email',)
	filter_horizontal = (
		'groups',
		'user_permissions',
	)
	readonly_fields = (
		'id',
		'last_login',
		'date_joined',
		'confirmation_sent_at',
	)
