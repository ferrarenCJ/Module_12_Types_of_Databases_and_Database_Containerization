import mysql.connector
from datetime import datetime
import sys

sys.dont_write_bytecode = True

if len(sys.argv) != 2:
    print("Usage: python update_rec.py <uuid>")
    sys.exit(1)

post_id = sys.argv[1]

cnx = mysql.connector.connect(
    user='root',
    password='RootPassword123',
    host='127.0.0.1',
    database='pluto',
    port=3306
)

cursor = cnx.cursor()

new_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

query = """
UPDATE posts
SET stamp = %s
WHERE id = %s
"""

cursor.execute(query, (new_stamp, post_id))

cnx.commit()

print(f"Rows updated: {cursor.rowcount}")

cursor.close()
cnx.close()