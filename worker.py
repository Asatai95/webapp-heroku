import os

import redis
from rq import Worker, Queue, Connection

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:8080')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    
