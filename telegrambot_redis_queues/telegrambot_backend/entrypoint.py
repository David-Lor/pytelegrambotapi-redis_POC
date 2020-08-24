"""BOT BACKEND - ENTRYPOINT
Main run entrypoint for the Updates Processor service
"""

# # Package # #
from .bot_worker import BotWorker

# # Project # #
from ..redis_queue import RedisQueue

__all__ = ("run",)


def run():
    queue = RedisQueue()
    queue.connect()
    bot = BotWorker(queue=queue)
    bot.loop()
