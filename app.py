# Contains App and routes
from flask import Flask
from flask_restful import Api
from resources.Index import Index

# App Config
app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(Index, '/')

if __name__ == "__main__":
    app.run(debug=True)
