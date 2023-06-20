import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

@app.route('/login/', methods = ['GET'])
def index():
    return render_template('login.html')

conn = psycopg2.connect(database = 'service_db',
 user = "postgres", password = "95299392", 
 host = "localhost", port= "5432")
cursor = conn.cursor()