"""TELEGRAM BOT BACKEND
The Backend receives the updates through a Redis Queue and processes them
"""

from .entrypoint import run as run_backend
