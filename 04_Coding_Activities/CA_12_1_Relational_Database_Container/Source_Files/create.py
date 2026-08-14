import mysql.connector
import sys

sys.dont_write_bytecode = True

cnx = mysql.connector.connect(
    user='root',
    password='RootPassword123',
    host='127.0.0.1',
    port=3306
)

# create cursor
cursor = cnx.cursor()

# delete previous db
query = "DROP DATABASE IF EXISTS restaurants"
cursor.execute(query)

# create db
query = "CREATE DATABASE IF NOT EXISTS restaurants"
cursor.execute(query)

# use db
query = "USE restaurants"
cursor.execute(query)

# create table with primary key
query = '''
CREATE TABLE restaurants (
    id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(20)
)
'''

cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()