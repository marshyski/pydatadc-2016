import redis

db = redis.StrictRedis('localhost', 6379, 1)
db.flushall()
