from collections.abc import Callable

from django.contrib.admin import AdminSite, ModelAdmin
from django.db.models import Model
from django.utils.translation import gettext_lazy as _


class ChatDiAdminSite(AdminSite):
	site_header = _('Chat:Di Administration Panel')
	site_title = _('Chat:Di Admin')
	index_title = _('Welcome to Chat:Di')

	def register_model(self, *models: type[Model]) -> Callable:
		def _model_admin_wrapper(admin_class: type[ModelAdmin]) -> type[ModelAdmin]:
			admin_class.admin = self  # type: ignore[attr-defined]
			self.register(models, admin_class)
			return admin_class

		return _model_admin_wrapper


admin_site = ChatDiAdminSite(name='chatdi_admin')
