from collections.abc import Callable

from django.conf import settings
from django.http import HttpRequest, HttpResponse

from ipware import get_client_ip


class RealIPMiddleware:
	"""
	Middleware to set the REMOTE_ADDR header to the real client IP address.
	This is useful when the application is behind a reverse proxy or load balancer.
	"""

	def __init__(self, get_response: Callable) -> None:
		self.get_response = get_response

	def __call__(self, request: HttpRequest) -> HttpResponse:
		ip, _ = get_client_ip(request, proxy_count=settings.PROXY_COUNT)
		if ip:
			request.META['REMOTE_ADDR'] = ip
		return self.get_response(request)
