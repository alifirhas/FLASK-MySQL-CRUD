from flask import Flask
from flask import jsonify
from flask_restful import Resource, reqparse
import mysql.connector

resources = Flask(__name__)

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'flask-mysql'
)

cursor = mydb.cursor(dictionary=True)

from resources import Index