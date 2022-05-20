import redis
import config


if __name__ == '__main__':
    with redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT) as redis_client:
        print(f'Random number was: {redis_client.brpop(config.QUEUE_NAME)}')
