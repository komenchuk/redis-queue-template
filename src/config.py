import os

from dotenv import load_dotenv


load_dotenv()
QUEUE_NAME = os.getenv('QUEUE_NAME')
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
