# pip install redis
import redis

# connect to server
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# read values
print("Italy:", r.get("Italy"))
print("France:", r.get("France"))