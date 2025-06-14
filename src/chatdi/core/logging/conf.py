from pathlib import Path
from typing import Any

DATETIME_FORMATTER = '%d/%b/%Y %H:%M:%S'


def get_log_formatter(debug: bool) -> str:
	if debug:
		return (
			'========== START ==========\n'
			'Time:    %(asctime)s\n'
			'Level:   %(levelname)s\n'
			'Logger:  %(name)s\n'
			'Func:    %(funcName)s\n'
			'Message: %(message)s\n'
			'==========  END  ==========\n'
		)
	return '[%(asctime)s] %(levelname)s in %(name)s.%(funcName)s:\n%(message)s\n'


def get_logging_config(debug: bool, log_dir: Path) -> dict[str, Any]:
	log_formatter = get_log_formatter(debug)
	logging: dict[str, Any] = {
		'version': 1,
		'disable_existing_loggers': False,
		'formatters': {
			'main': {
				'format': log_formatter,
				'datefmt': DATETIME_FORMATTER,
			},
		},
		'filters': {
			'sql_formatter': {
				'()': 'core.logging.filters.SQLFormatterFilter',
			},
		},
		'handlers': {
			'console': {
				'level': 'WARNING',
				'class': 'logging.StreamHandler',
				'formatter': 'main',
			},
			'timed_rotating_file': {
				'level': 'DEBUG',
				'class': 'logging.handlers.TimedRotatingFileHandler',
				'filename': log_dir / 'main.log',
				'formatter': 'main',
				'when': 'midnight',
				'interval': 1,
				'backupCount': 7,
			},
			'telegram': {
				'level': 'DEBUG',
				'class': 'core.logging.handlers.TelegramHandler',
				'formatter': 'main',
			},
			'celery_file': {
				'level': 'DEBUG',
				'class': 'logging.handlers.TimedRotatingFileHandler',
				'filename': log_dir / 'celery.log',
				'formatter': 'main',
				'when': 'midnight',
				'interval': 1,
				'backupCount': 7,
			},
			'db_file': {
				'level': 'DEBUG',
				'class': 'logging.handlers.TimedRotatingFileHandler',
				'filename': log_dir / 'db.log',
				'formatter': 'main',
				'filters': ['sql_formatter'],
				'when': 'midnight',
				'interval': 1,
				'backupCount': 7,
			},
		},
		'loggers': {
			'django': {
				'handlers': ['console'],
				'level': 'DEBUG',
				'propagate': False,
			},
			'celery': {
				'handlers': ['console'],
				'level': 'INFO',
				'propagate': False,
			},
			'main': {
				'handlers': ['console'],
				'level': 'DEBUG',
				'propagate': False,
			},
			'telegram': {
				'handlers': ['console'],
				'level': 'DEBUG',
				'propagate': False,
			},
			'db_logger': {
				'handlers': ['console'],
				'level': 'INFO',
				'propagate': False,
				'filters': ['sql_formatter'],
			},
		},
	}
	if not debug:
		logging['loggers']['django']['handlers'] = ['console', 'timed_rotating_file']
		logging['loggers']['django']['level'] = 'ERROR'
		logging['loggers']['celery']['handlers'] = ['console', 'celery_file']
		logging['loggers']['main']['handlers'] = ['console', 'timed_rotating_file']
		logging['loggers']['telegram']['handlers'] = ['console', 'telegram']
		logging['loggers'].pop('db_logger', None)
	return logging
