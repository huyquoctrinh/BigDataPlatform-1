import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, retry_on_timeout=True)

print(redis_client.ping())
print("Connected to Redis")