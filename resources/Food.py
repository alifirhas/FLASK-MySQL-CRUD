from flask_restful import Resource

class Food(Resource):
    def get(self):
        return {
            "data": "Food getted"
        }
    def post(self):
        return {
            "data": "Food posted"
        }