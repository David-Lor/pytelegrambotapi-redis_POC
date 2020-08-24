.DEFAULT_GOAL := help

run-redis: ## docker run redis in background (create & start new container)
	docker run -it -d --name=redis -p 127.0.0.1:6379:6379 redis

start-redis: ## docker start redis (start existing container)
	docker start redis

stop-redis: ## docker stop redis (stop existing running container)
	docker stop redis

rm-redis: ## docker rm redis (remove existing stopped container)
	docker rm redis

teardown-redis: ## docker stop & rm redis (stop & remove existing container)
	docker stop redis
	docker rm redis

run-polling: ## run bot polling in foreground
	python run_bot_polling.py

run-worker: ## run bot updates worker in foreground
	python run_bot_worker.py

create-conda-env: ## conda create from conda-env.yml file
	conda env create --file conda-env.yml

help: ## show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
