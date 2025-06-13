from logging import Handler, LogRecord
from os import getenv
from threading import Thread

from telebot import TeleBot
from telebot.util import antiflood

MAX_MESSAGE_LENGTH = 4096
TELEGRAM_LOG_BOT_TOKEN = getenv('TELEGRAM_LOG_BOT_TOKEN', '')
TELEGRAM_LOG_CHAT_ID = getenv('TELEGRAM_LOG_CHAT_ID', '')
log_bot = TeleBot(TELEGRAM_LOG_BOT_TOKEN)


class TelegramHandler(Handler):
	def __init__(self) -> None:
		super().__init__()
		self.bot = log_bot
		self.chat_id = TELEGRAM_LOG_CHAT_ID
		self.MAX_MESSAGE_LENGTH = MAX_MESSAGE_LENGTH

	def emit(self, record: LogRecord) -> None:
		thread = Thread(target=self.send_log_message, args=(record,), daemon=True)
		thread.start()

	def send_log_message(self, record: LogRecord) -> None:
		try:
			log_entry = self.format(record)
			for i in range(0, len(log_entry), self.MAX_MESSAGE_LENGTH):
				antiflood(
					self.bot.send_message,
					self.chat_id,
					log_entry[i : i + self.MAX_MESSAGE_LENGTH],
				)
		except Exception:
			self.handleError(record)
