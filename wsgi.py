from flask import Flask, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)



app.run(host='127.0.0.1', port='8080', debug=True)
    