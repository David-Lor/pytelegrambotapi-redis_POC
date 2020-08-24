"""TELEGRAM BOT HANDLERS
Definition of Bot handler functions
"""

# # Native # #
import asyncio
import random

# # Installed # #
from telebot.types import Message

# # Project # #
from ..telegram_bot import Bot

__all__ = ("register_handlers",)


def register_handlers(bot: Bot):
    """Register Telegram Bot handlers for updates.
    The handler functions are defined within, with decorators"""

    @bot.message_handler(commands=["help"])
    def _help_command_handler(message: Message, *args, **kwargs):
        print("/help command handler")
        bot.reply_to(message=message, text="I'm helping you!")

    @bot.message_handler(func=lambda m: True)
    def _global_message_handler(message: Message, *args, **kwargs):
        print("Global message handler")
        bot.reply_to(
            message=message,
            text=f"Received your message! (<pre>{message.text}</pre>)",
            parse_mode="HTML"
        )
