from flask_restful import Resource

class User(Resource):
    def get(self):
        return {
            "data": "User getted"
        }
    def post(self):
        return {
            "data": "User posted"
        }