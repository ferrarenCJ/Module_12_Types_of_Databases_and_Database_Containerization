import mysql.connector
import sys


sys.dont_write_bytecode = True

cnx = mysql.connector.connect(
    host='localhost', 
    port=3306,
    user='mysqluser',
    password='UserPassword123',
    auth_plugin='mysql_native_password'
    )

# create cursor
cursor = cnx.cursor()

# insert
query = ("SHOW DATABASES")
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# clean up
cursor.close()
cnx.close()    