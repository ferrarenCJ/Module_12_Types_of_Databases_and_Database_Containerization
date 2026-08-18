import mysql.connector
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(
    user='root',
    password='MyNewPass',
    host='127.0.0.1',
    port=3300,
    auth_plugin='mysql_native_password'
)

# create cursor
cursor = cnx.cursor()

# delete previous db
query = ("DROP DATABASE IF EXISTS `gas_utility_assets`;")
cursor.execute(query)

# create db
query = ("CREATE DATABASE IF NOT EXISTS gas_utility_assets")
cursor.execute(query)

# use db
query = ("USE gas_utility_assets")
cursor.execute(query)

# create table
query = ('''
CREATE TABLE assets(
    asset_id INT PRIMARY KEY,
    asset_type VARCHAR(50),
    location VARCHAR(50)
)
''')

cursor.execute(query)

query = """
INSERT INTO assets
VALUES
(1, 'Regulator', 'Anaheim'),
(2, 'Valve', 'Pico Rivera'),
(3, 'Meter', 'Santa Ana')
"""
cursor.execute(query)


# clean up
cnx.commit()
cursor.close()
cnx.close()    