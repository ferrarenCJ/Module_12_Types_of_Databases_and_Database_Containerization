# pip install redis
import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

r.mset({
    "Milk": "Lactose",
    "Bread": "Gluten"
})

print("Values written successfully.")