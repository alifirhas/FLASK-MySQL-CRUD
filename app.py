# Contains App and routes
from flask import Flask
from flask_restful import Api
from resources.Index import Index
from resources.Files import Files
import os
from dotenv import load_dotenv

# App Config
app = Flask(__name__)
api = Api(app)
load_dotenv()

# Routes
api.add_resource(Index, '/')
api.add_resource(Files, '/file')

if __name__ == "__main__":
    app.run(debug=(os.getenv('DEBUG') == 'True'))
