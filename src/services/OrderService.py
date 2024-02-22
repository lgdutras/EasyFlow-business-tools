from ..repositories.OrderRepository import OrderRepository

class OrderService():

    def newOrder(document):
        return OrderRepository.createOrder(document)
    
    def cancelOrder(id_order):
        return OrderRepository.cancelOrder(id_order)
