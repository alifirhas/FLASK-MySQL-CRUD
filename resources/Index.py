from multiprocessing import connection
from flask import jsonify
from flask_restful import Resource, reqparse
from pkg_resources import require
from common.connection import mydb, cursor

user_parser_post = reqparse.RequestParser()
user_parser_post.add_argument("id", type=str, help="ID pengguna")
user_parser_post.add_argument("nama", type=str, help="Nama pengguna", required=True)
user_parser_post.add_argument("username", type=str, help="Username pengguna", required=True)
user_parser_post.add_argument("password", type=str, help="Password pengguna", required=True)

user_parser_delete = reqparse.RequestParser()
user_parser_delete.add_argument("id", type=str, help="ID Pengguna", required=True)

class Index(Resource):

    def get(self):
        """Mengambil semua data

        Returns:
            JSON: Semua data dalam table berbentuk JSON
        """
        
        cursor.execute('SELECT * FROM user')
        result = {
            "objects": cursor.fetchall()
        }
        
        return jsonify(result)

    def post(self):
        """Memasukkan sebuah data
        
        Args:
            nama (str): nama pengguna
            username (str): username pengguna
            password (str): password pengguna

        Returns:
            JSON: Data terakhir masuk
        """
        
        args = user_parser_post.parse_args()

        sql = "INSERT INTO user (nama, username, password) VALUES (%s, %s, %s)"
        val = (args.nama, args.username, args.password)
        cursor.execute(sql, val)
        mydb.commit()
        
        lastRow = cursor.lastrowid
        
        sql = "SELECT * FROM user where id=" + str(lastRow)
        cursor.execute(sql)

        return jsonify(cursor.fetchone())

    def put(self):
        """Mengubah sebuah data
        
        Args:
            id (id): id pengguna
            nama (str): nama pengguna
            username (str): username pengguna
            password (str): password pengguna

        Returns:
            JSON: Data yang diubah
        """
        
        args = user_parser_post.parse_args()
        
        sql = "UPDATE user SET nama=%s,username=%s,password=%s WHERE id=" + str(args.id)
        val = (args.nama, args.username, args.password)
        cursor.execute(sql, val)
        mydb.commit()
        
        sql = "SELECT * FROM user where id=" + str(args.id)
        cursor.execute(sql)
        
        return jsonify(cursor.fetchone())

    def delete(self):
        """Menghapus sebuah data
        
        Args:
            id (id): id pengguna

        Returns:
            None: 
        """
        
        args = user_parser_delete.parse_args()
        
        sql = "DELETE FROM user WHERE id=" + str(args.id)
        cursor.execute(sql)
        mydb.commit()
        
