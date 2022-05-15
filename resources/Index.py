from flask_restful import Resource

class Index(Resource):
    def get(self):
        return {
            "data": "Get data"
        }
    def post(self):
        return {
            "data": "Post data"
        }
    def put(self):
        return {
            "data": "Put data"
        }
    def delete(self):
        return {
            "data": "Delete data"
        }