"""TELEGRAM BOT
Custom class for a Telegram Bot
"""

# # Native # #
import asyncio

# # Installed # #
import telebot

# # Package # #
from .settings import telegram_settings
from .redis_queue import RedisQueue

__all__ = ("Bot",)


class Bot(telebot.TeleBot):
    """A Telegram Bot. This class inherits from pytelegrambotapi TeleBot,
    loading the Telegram Bot token from environment variable (through project settings).
    Must be initialized with an existing RedisQueue object"""
    def __init__(self, queue: RedisQueue, **kwargs):
        kwargs.setdefault("token", telegram_settings.token)
        super().__init__(**kwargs)

        self._queue = queue
        self._loop_stop_event = asyncio.Event()

    async def _loop_worker(self):
        """Main loop logic, to be override by inheritor classes"""
        # NOTE To be implemented by inheritor classes
        self._loop_stop_event.set()

    async def async_loop(self):
        """Start running the loop asynchronously"""
        while not self._loop_stop_event.is_set():
            await self._loop_worker()

    def loop(self):
        """Start running the loop synchronously, in foreground"""
        asyncio.get_event_loop().run_until_complete(self.async_loop())
