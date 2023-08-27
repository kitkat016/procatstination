import mysql.connector

# File only needs to be run once to connect database to MySQL

# Password will need to be changed
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Spider7',
    database='characters'
)

my_cursor = mydb.cursor()


my_cursor.execute("SELECT * FROM user")

my_result = my_cursor.fetchall()

for x in my_result:
    print(x)
