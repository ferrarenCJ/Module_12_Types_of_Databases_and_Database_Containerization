# pip install redis
import redis

# connect to server
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# create key-value pairs
r.mset({
    "Italy": "Rome",
    "France": "Paris"
})

print("Dictionary created successfully.")