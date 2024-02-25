from ..repositories.OrderRepository import OrderRepository

class OrderService():

    def newOrder(document):
        return OrderRepository.createOrder(document)
    
    def cancelOrder(id_order):
        return OrderRepository.cancelOrder(id_order)
    
    def includeItem(id_order, id_product, quantity):
        order_repository = OrderRepository()
        return order_repository.includeItem(id_order, id_product, quantity)
    
    def removeItem(id_product, id_order):
        order_repository = OrderRepository()
        return order_repository.removeItem(id_product, id_order)
