import logging

import sqlparse


class SQLFormatterFilter(logging.Filter):
	def filter(self, record: logging.LogRecord) -> bool:
		formatted_message = record.getMessage()
		record.msg = sqlparse.format(
			formatted_message,
			reindent=True,
			keyword_case='upper',
			indent_width=4,
		)
		record.args = ()
		return True
