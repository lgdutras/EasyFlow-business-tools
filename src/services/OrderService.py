from ..repositories.OrderRepository import OrderRepository

class OrderService():

    def newOrder(document):
        return OrderRepository.createOrder(document)

