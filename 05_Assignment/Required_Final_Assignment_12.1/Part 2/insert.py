import mysql.connector
import sys

sys.dont_write_bytecode = True

cnx = mysql.connector.connect(
    user='root',
    password='MyNewPass',
    host='127.0.0.1',
    port=3300,
    database='gas_utility_assets',
    auth_plugin='mysql_native_password'
)

# create cursor
cursor = cnx.cursor()

# insert a new record
query = """
INSERT INTO assets
VALUES
(4, 'Regulator Station', 'Long Beach')
"""

cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()

print("Record inserted successfully.")

