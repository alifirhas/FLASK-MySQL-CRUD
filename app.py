# Contains App and routes
from flask import Flask
from flask_restful import Api
from resources import resources
import os
from dotenv import load_dotenv

load_dotenv()

# App Config
app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(resources.Index, '/')

if __name__ == "__main__":
    app.run(debug=os.getenv("debug"))
