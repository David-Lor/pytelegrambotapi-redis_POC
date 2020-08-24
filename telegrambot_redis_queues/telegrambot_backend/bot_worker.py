"""BOT WORKER
Custom class for the Bot Worker Updates Processor
"""

# # Native # #
import pickle

# # Package # #
from .handlers import register_handlers

# # Project # #
from ..telegram_bot import Bot

__all__ = ("BotWorker",)


class BotWorker(Bot):
    """The Bot Worker receives enqueued updates from a Redis Queue, and process them through the handlers defined"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        register_handlers(self)

    async def _loop_worker(self):
        """Get update from the queue, unpickle it and process on the bot"""
        update_bytes = await self._queue.get()
        update = pickle.loads(update_bytes)
        self.process_new_updates([update])
