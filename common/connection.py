import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='flask-mysql'
)

cursor = mydb.cursor(dictionary=True)