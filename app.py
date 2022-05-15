# Contains App and routes
from flask import Flask
from flask_restful import Api
from resources.Food import Food
from resources.User import User
from resources.Index import Index

app = Flask(__name__)
api = Api(app)

api.add_resource(Index, '/')
api.add_resource(Food, '/Food')
api.add_resource(User, '/User')

if __name__ == "__main__":
    app.run(debug=True)