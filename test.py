import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "")

response = requests.post(BASE + "", {
    "nama": "gege",
    "password": "gege",
    "username": "gege"
})

print(response.json())

# import mysql.connector

# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '',
#     database = 'flask-mysql'
# )

# cursor = mydb.cursor()
# cursor.execute('SELECT * FROM user')

# for item in cursor:
#     print(item)
