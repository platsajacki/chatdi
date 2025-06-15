from django.conf import settings
from drf_spectacular.utils import extend_schema

from core.spectacular.constants import SchemaTag
from humanize import precisedelta

ACCESS_TOKEN_LIFETIME = precisedelta(settings.ACCESS_TOKEN_LIFETIME)
REFRESH_TOKEN_LIFETIME = precisedelta(settings.REFRESH_TOKEN_LIFETIME)

token_obtain_pair_view = extend_schema(
	tags=[SchemaTag.AUTHENTICATION.value],
	methods=['post'],
	description=(
		'Takes a set of user credentials and returns an access and refresh JSON web token pair '
		'to prove the authentication of those credentials.'
		f'<br><b>Livetime: {ACCESS_TOKEN_LIFETIME} for access token, '
		f'{REFRESH_TOKEN_LIFETIME} for refresh token.</b>'
	),
)

token_refresh_view = extend_schema(tags=[SchemaTag.AUTHENTICATION.value], methods=['post'])
