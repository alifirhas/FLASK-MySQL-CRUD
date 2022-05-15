from flask_restful import Resource

class Index(Resource):
    def get(self):
        return {
            "data": "Welcome to this world of mine"
        }