from drf_spectacular.utils import extend_schema

from core.spectacular.constants import SchemaTag

privat_schema_view = extend_schema(tags=[SchemaTag.PRIVATE.value], methods=['get'])
