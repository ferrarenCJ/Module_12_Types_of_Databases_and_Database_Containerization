
from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['localhost'], port=9042)

session = cluster.connect('books')

# Query all books
rows = session.execute("""
    SELECT * FROM book
""")

# Display results
for row in rows:
    print(row)