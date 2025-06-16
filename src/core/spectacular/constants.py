from enum import Enum


class SchemaTag(str, Enum):
	PRIVATE = 'Private'
	PUBLIC = 'Public'
	AUTHENTICATION = 'Authentication'
