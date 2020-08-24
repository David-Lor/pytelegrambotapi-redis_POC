# pytelegrambotapi + redis queue POC

This is a Proof Of Concept of a Telegram Bot working with Redis queues,
where one service receives client updates from Telegram Bot API and pushes them into a Redis queue.
Then, one or more backend services subscribe to the queue and process the incoming updates.

## Services intended to be deployed

- 1/n Redis server (cluster?)
- 1 Telegram updates entrypoint service (telegrambot_entrypoint): receives Telegram bot client updates through polling/webhook and insert them into a Redis queue (it would be interesting to have more of these workers for redundancy, but only one should run at the same time)
- n Telegram bot backend services/workers (telegrambot_backend): subscribe to the queue and get the requests processed through aiogram

## Getting started

```bash
# 1) Create conda env (optional)
make create-conda-env
conda activate pytelegrambotapi+redis

# 2) Start a Redis server (requires Docker)
make run-redis

# 3) Setup .env file
cp sample.env .env
# Edit the .env file to change the TOKEN to the token of a bot of your own

# 4) Run bot polling
make run-polling

# 5) Run a bot updates worker (new terminal - you can run as many as you want!)
conda activate pytelegrambotapi+redis
make run-worker

# After playing with it... Teardown of Redis server (stop & remove container)
make teardown-redis
```

## TODO

- Replace aioredis with sync redis (as pytelegrambot does not run async) & set all functions sync
- Improve logging
- Improve multithreading for each bot worker + add commands that sleep for a few seconds
