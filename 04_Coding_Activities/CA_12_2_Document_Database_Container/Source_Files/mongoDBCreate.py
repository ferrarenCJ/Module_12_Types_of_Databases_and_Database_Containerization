from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.EmployeeDB

collection = db.employees

employeeCollection = [
    {"FirstName": "John", "LastName": "Smith", "Age": 25},
    {"FirstName": "Peter", "LastName": "Smith", "Age": 26},
    {"FirstName": "Gabriel", "LastName": "Smith", "Age": 28},
    {"FirstName": "Penny", "LastName": "Lane", "Age": 22},
    {"FirstName": "Eleanor", "LastName": "Rigby", "Age": 23},
    {"FirstName": "Helen", "LastName": "Rose", "Age": 23}
]

collection.delete_many({})

result = collection.insert_many(employeeCollection)

if "EmployeeDB" in client.list_database_names():
    print("Employee database created!")

print(result.inserted_ids)