"""UPDATES RECEIVER - ENTRYPOINT
Main run entrypoint for the Updates Receiver service
"""

# # Package # #
from .bot_receiver import BotReceiver

# # Project # #
from ..redis_queue import RedisQueue

__all__ = ("run",)


def run():
    queue = RedisQueue()
    queue.connect()
    bot = BotReceiver(queue=queue)
    bot.loop()
