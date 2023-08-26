import mysql.connector

# File only needs to be run once to connect database to MySQL

# Password will need to be changed
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Spider7'
)

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE characters")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)