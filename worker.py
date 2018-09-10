import os

import redis
from rq import Worker, Queue, Connection

listen = 'https://www.googleapis.com/auth/calendar.readonly'

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:8080')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
