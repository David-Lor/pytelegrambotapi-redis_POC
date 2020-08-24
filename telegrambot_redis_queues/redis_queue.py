"""REDIS QUEUE
Custom class for a Redis Queue
"""

# # Native # #
import asyncio

# # Installed # #
import aioredis
from aioredis import Redis

# # Package # #
from .settings import redis_settings

__all__ = ("RedisQueue",)


class RedisQueue:
    """A Redis Queue.
    This class creates a Redis object, where objects can be enqueued or fetched from the queue.
    Settings for Redis connection and queue are loaded from environment variables (through project settings)"""
    _url: str
    _queue_name: str
    _redis: Redis

    def __init__(self, url=redis_settings.url, queue_name=redis_settings.queue_name):
        self._url = url
        self._queue_name = queue_name

    def connect(self):
        asyncio.get_event_loop().run_until_complete(self._async_connect())

    async def _async_connect(self):
        self._redis = await aioredis.create_redis_pool(self._url)

    async def enqueue(self, data):
        await self._redis.rpush(self._queue_name, data)
        print("Enqueued")

    async def get(self):
        r = await self._redis.blpop(self._queue_name)
        data = r[1]
        print("Received")
        return data
