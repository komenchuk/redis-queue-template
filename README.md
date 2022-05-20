# Redis Queue Template

*This repository contains a template for creating a queue in Redis*

## Dependencies

- Virtual environment with Python ≥ 3.6 (tested on Linux with Python 3.8.10)

## Install requirements

`pip install -r requirements.txt`

## Environment variables in dotenv

Create `.env` file in the root of repository with following variables:

    - `QUEUE_NAME`: queue key name
    - `REDIS_HOST`: host for Redis deploy
    - `REDIS_PORT`: port for Redis deploy

## Run Redis

`docker run -p 6379:6379 redis:latest`

## Run producer

`python src/producer.py`

## Run consumer

`python src/consumer.py`
