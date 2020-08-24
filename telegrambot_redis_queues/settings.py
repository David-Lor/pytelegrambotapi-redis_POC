"""SETTINGS
Common settings shared by both services, using pydantic BaseSettings,
loading them from environment variables or .env file
"""

# # Installed # #
import pydantic

__all__ = ("telegram_settings", "redis_settings")


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class TelegramSettings(BaseSettings):
    token: str

    class Config(BaseSettings.Config):
        env_prefix = "BOT_"


class RedisSettings(BaseSettings):
    url: str = "redis://localhost:6379"
    queue_name: str = "TelegramBotQueue"


telegram_settings = TelegramSettings()
redis_settings = RedisSettings()
