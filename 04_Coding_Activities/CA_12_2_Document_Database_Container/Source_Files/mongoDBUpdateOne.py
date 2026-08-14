
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# Connect to EmployeeDB
db = client.EmployeeDB

# Connect to employees collection
collection = db.employees

# Create filter
filter = {
    "LastName": "Rose"
}

# Create new values
newvalues = {
    "$set": {
        "Age": 32
    }
}

# Update employee
collection.update_one(filter, newvalues)

# Display all employees
employeeCursor = collection.find()

for employee in employeeCursor:
    print(employee)