# from flask import jsonify
# from flask_restful import Resource, reqparse
# import mysql.connector

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='flask-mysql'
# )

# cursor = mydb.cursor(dictionary=True)

from resources import resources

user_parser_post = reqparse.RequestParser()
user_parser_post.add_argument("nama", type=str, help="Nama pengguna", required=True)
user_parser_post.add_argument("username", type=str, help="Username pengguna", required=True)
user_parser_post.add_argument("password", type=str, help="Password pengguna", required=True)

class Index(Resource):
    def get(self):
        cursor.execute('SELECT * FROM user')
        result = {
            "objects": cursor.fetchall()
        }
        
        return jsonify(result)

    def post(self):
        args = user_parser_post.parse_args()

        sql = "INSERT INTO user (nama, username, password) VALUES (%s, %s, %s)"
        val = (args.nama, args.username, args.password)
        cursor.execute(sql, val)

        mydb.commit()

        return {
            "yey": "ehll"
        }

    def put(self):
        return {
            "data": "Put data"
        }

    def delete(self):
        return {
            "data": "Delete data"
        }
