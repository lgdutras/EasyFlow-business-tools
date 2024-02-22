from ..services.OrderService import OrderService
from flask import request
from flask_restful import Resource

class OrderController():

    class newOrder(Resource):
        def put(self):
            return OrderService.newOrder(request.args.get('document'))
