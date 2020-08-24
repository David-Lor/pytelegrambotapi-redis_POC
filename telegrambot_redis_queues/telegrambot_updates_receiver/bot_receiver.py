"""BOT RECEIVER
Custom class for the Telegram Bot Updates Receiver
"""

# # Native # #
import asyncio
import pickle

# # Project # #
from ..telegram_bot import Bot

__all__ = ("BotReceiver",)


class BotReceiver(Bot):
    """The Bot Receiver gets updates from Telegram (polling), and enqueues them in Redis"""
    def __init__(self, loop_frequency=1, **kwargs):
        super().__init__(**kwargs)
        self._loop_frequency = loop_frequency
        self._last_update_id = None
        """The Update ID for the last fetched update must be saved,
        so when calling get_updates again it will not return already processed (enqueued) updates"""

    async def _loop_worker(self):
        """Get updates from Telegram, and enqueue them using pickle"""
        # TODO wrap around try/except for connection issues
        updates = self.get_updates(offset=self._last_update_id)
        # NOTE security concerns for using pickle (find alternatives?)
        await asyncio.gather(
            *[self._queue.enqueue(pickle.dumps(update)) for update in updates],
            asyncio.sleep(self._loop_frequency)
        )
        if updates:
            self._last_update_id = max(update.update_id for update in updates) + 1
