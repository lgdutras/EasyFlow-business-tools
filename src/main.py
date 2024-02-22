from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from src.controllers.CustomerController import CustomerController
from src.controllers.OrderController import OrderController
import json
        
app = Flask(__name__)
api = Api(app)

#Customers Endpoints
api.add_resource(CustomerController, '/customers/findByDocument')

#Orders Endpoints
api.add_resource(OrderController.newOrder, '/orders/new')

if __name__ == "__main__":
    app.run()