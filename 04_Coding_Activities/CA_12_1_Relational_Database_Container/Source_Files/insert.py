import mysql.connector
from datetime import datetime
import sys

sys.dont_write_bytecode = True

cnx = mysql.connector.connect(
    user='root',
    password='RootPassword123',
    host='127.0.0.1',
    database='restaurants',
    port=3306
)

# create cursor
cursor = cnx.cursor()

# insert record
id = "1"
name = datetime.now().strftime('%H:%M:%S')

query = f'INSERT INTO restaurants VALUES("{id}", "{name}")'

cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()

print("Restaurant record inserted successfully.")
