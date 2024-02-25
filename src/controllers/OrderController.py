from ..services.OrderService import OrderService
from flask import request
from flask_restful import Resource

class OrderController():

    class newOrder(Resource):
        def put(self):
            return OrderService.newOrder(request.args.get('document'))
    
    class cancelOrder(Resource):
        def delete(self):
            return OrderService.cancelOrder(request.args.get('id_order'))
        
    class includeItem(Resource):
        def put(self):

            id_order = request.args.get('id_order')
            id_product = request.args.get('id_product')
            quantity = request.args.get('quantity')

            return OrderService.includeItem(id_order, id_product, quantity)

    class removeItem(Resource):
        def delete(self):

            id_order = request.args.get('id_order')
            id_product = request.args.get('id_product')

            return OrderService.removeItem(id_order=id_order, id_product=id_product)
        
    class updateQuantity(Resource):
        def patch(self):

            id_order = request.args.get('id_order')
            id_product = request.args.get('id_product')
            quantity = request.args.get('quantity')

            return OrderService.updateQuantity(id_order, id_product, quantity)