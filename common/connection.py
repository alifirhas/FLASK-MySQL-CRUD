import mysql.connector
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.dirname(__file__) + '/../config.ini')

mydb = mysql.connector.connect(
    host=config['Database']['Host'],
    user=config['Database']['User'],
    password=config['Database']['Password'],
    database=config['Database']['DBName']
)

cursor = mydb.cursor(dictionary=True)