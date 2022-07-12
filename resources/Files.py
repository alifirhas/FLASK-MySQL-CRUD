import os
from flask import jsonify
from flask_restful import Resource, reqparse
from common.connection import mydb, cursor
import werkzeug
from dotenv import load_dotenv
import uuid

file_parser = reqparse.RequestParser()
file_parser.add_argument("picture", type=werkzeug.datastructures.FileStorage, location='files', help="File")
file_parser.add_argument("halo", type=str, help="Nama pengguna", required=True)

class Files(Resource):

    def get(self):
        
        cursor.execute('SELECT * FROM files')
        
        result = {
            "objects": cursor.fetchall()
        }
        
        return jsonify(result)

    def post(self):
        args = file_parser.parse_args()
        
        # Mengambil file dari arguments
        # Beri nama baru secara random
        # Dan upload ke directory UPLOAD_FOLDER
        file = args['picture']
        file_name = file.filename
        file_ext = file_name.split(".")[1]
        file_name = str(uuid.uuid4()) + "." + file_ext
        file.save(os.path.join(os.getenv('UPLOAD_FOLDER'), file_name))
        
        # print(file.filename)
        

    def put(self):
        return {
            "objects": "This is file"
        }

    def delete(self):
        return {
            "objects": "This is file"
        }
        
