from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from src.controllers.CustomerController import CustomerController
from src.controllers.OrderController import OrderController
import json
        
app = Flask(__name__)
api = Api(app)

class Status(Resource):
    parser = reqparse.RequestParser()
    def get(self):
        return {'Status': 'Online'}
    
#Check API Status on home
api.add_resource(Status, '/')

#Customers Endpoints
api.add_resource(CustomerController, '/customers/findByDocument')

#Orders Endpoints
api.add_resource(OrderController.newOrder, '/orders/new')
api.add_resource(OrderController.cancelOrder, '/orders/cancel')
api.add_resource(OrderController.includeItem, '/orders/items/include')

if __name__ == "__main__":
    app.run()