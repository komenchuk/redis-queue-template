import random

import redis
import config


if __name__ == '__main__':
    with redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT) as redis_client:
        redis_client.lpush(config.QUEUE_NAME, random.randint(0, 999))
