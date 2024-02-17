from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from src.controllers.CustomerController import CustomerController
import json
        
app = Flask(__name__)
api = Api(app)

api.add_resource(CustomerController, '/customers/findByDocument')

if __name__ == "__main__":
    app.run()