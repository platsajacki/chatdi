from abc import ABCMeta, abstractmethod
from collections.abc import Callable
from typing import Any


class BaseService(metaclass=ABCMeta):
	"""Base service template.

	All services in the app should follow these rules:
		- Input variables should be defined at initialization (__init__).
		- The service should implement a single entrypoint without arguments.

	Example:
	- This is ok:
		```
			@dataclass
			class UserCreator(BaseService):
				first_name: str
				last_name: str | None

				def act(self) -> User:
					return User.objects.create(
						first_name=self.first_name,
						last_name=self.last_name,
					)


			# Usage:
			# user = UserCreator(first_name="Ivan", last_name="Petrov")()
		```

	- This is not ok:
		```
			class UserCreator:
				def __call__(
					self, first_name: str, last_name: str | None
				) -> User:
					return User.objects.create(
						first_name=self.first_name,
						last_name=self.last_name,
					)
		```
	"""

	def __call__(self) -> Any:
		self.validate()
		return self.act()

	def get_validators(self) -> list[Callable]:
		return []

	def validate(self) -> None:
		for validator in self.get_validators():
			validator()

	@abstractmethod
	def act(self) -> Any:
		raise NotImplementedError('Please implement in the service class')
