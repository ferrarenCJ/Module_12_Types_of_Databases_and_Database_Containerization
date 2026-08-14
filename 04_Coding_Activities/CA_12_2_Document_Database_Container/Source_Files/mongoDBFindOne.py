
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.EmployeeDB

collection = db.employees

employee = collection.find_one(
    {"LastName": "Rigby"}
)

print(employee)