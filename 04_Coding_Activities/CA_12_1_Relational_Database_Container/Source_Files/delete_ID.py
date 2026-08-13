import mysql.connector
import sys

cnx = mysql.connector.connect(
    user='root',
    password='RootPassword123',
    host='127.0.0.1',
    database='pluto',
    port=3306
)

cursor = cnx.cursor()

post_id = sys.argv[1]

query = """
DELETE FROM posts
WHERE id = %s
"""

cursor.execute(query, (post_id,))

cnx.commit()

print(f"Rows deleted: {cursor.rowcount}")

cursor.close()
cnx.close()