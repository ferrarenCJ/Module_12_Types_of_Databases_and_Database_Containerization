# pip install redis
import redis

# connect to server
r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

# read values
print("Milk:", r.get("Milk"))
print("Bread:", r.get("Bread"))