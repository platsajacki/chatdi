from drf_spectacular.utils import extend_schema

from core.spectacular.constants import SchemaTag

token_obtain_pair_view = extend_schema(tags=[SchemaTag.AUTHENTICATION.value], methods=['post'])
token_refresh_view = token_obtain_pair_view
