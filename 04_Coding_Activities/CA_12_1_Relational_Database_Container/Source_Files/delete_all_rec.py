import mysql.connector
import sys

sys.dont_write_bytecode = True

cnx = mysql.connector.connect(
    user='root',
    password='RootPassword123',
    host='127.0.0.1',
    database='pluto',
    port=3306
)

# create cursor
cursor = cnx.cursor()

# delete all records
query = "DELETE FROM posts"
cursor.execute(query)

# save changes
cnx.commit()

print(f"Rows deleted: {cursor.rowcount}")

# clean up
cursor.close()
cnx.close()