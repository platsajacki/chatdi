from django.conf import settings

from redis.asyncio import Redis

redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=4, decode_responses=True)
