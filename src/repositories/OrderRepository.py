from ..adapters.OrderAdapter import OrderAdapter, OrderItemAdapter
from ..repositories.CustomerRepository import CustomerRepository
from ..repositories.ProductRepository import ProductRepository
from ..resources.dbconfig import Session
from flask import abort, jsonify
from requests import status_codes


class OrderRepository():

    def __init__(self):

        self.order_status = {
                            0: 'canceled',
                            1: 'opened',
                            2: 'queued',
                            3: 'preparing',
                            4: 'delivered',
                            5: 'closed',
                            6: 'returned'
                            }

    def createOrder(document=''):
        session = Session()
        try:
            id_customer = '' if status_codes == 404 else CustomerRepository.getIdByDocument(document).id_customer

            newOrder = OrderAdapter(
                                    order_status=1,
                                    id_customer=id_customer)
            session.add(newOrder)
            session.commit()

            orderToInclude = {
                        'msg': 'New order opened',
                        'id_order': newOrder.id_order,
                        'id_customer': newOrder.id_customer,
                        'order_status': newOrder.order_status,
                        }

            return jsonify(orderToInclude)
        
        except Exception as e:
            session.rollback()
            return abort(404, str(e))
        
    def cancelOrder(id_order):

        session = Session()
        orderTocancel = session.query(OrderAdapter).filter_by(id_order=id_order).first()

        if orderTocancel == None:

            return abort(404, 'Order with id %s does not exists' % id_order)
        
        elif str(orderTocancel.order_status) == str(0):

            return abort(409, 'Order %s is already canceled' % id_order)
        else:
            
            orderTocancel.order_status = 0
            session.commit()

            return jsonify({'msg': 'Order Canceled',
                            'id_order': orderTocancel.id_order})
        
    def includeItem(self, id_order, id_product, quantity):

        session = Session()
        orderToInclude = session.query(OrderAdapter).filter_by(id_order=id_order).first()

        if orderToInclude == None:

            return abort(404, 'Order with id %s does not exists' % id_order)
        
        elif orderToInclude.order_status not in (1, 2):
            order_status = orderToInclude.order_status
            order_status_description = self.order_status.get(order_status)
            return abort(423, 'You can not include items on a order wich is %s' % (order_status_description))
        
        product = ProductRepository.getProductById(id_product)
        newItem = OrderItemAdapter(
                                    id_order = id_order,
                                    id_product = id_product,
                                    price = product.price,
                                    quantity = quantity
                                   )
        
        session.add(newItem)
        session.commit()

        return jsonify({
            'id_product': newItem.id_product,
            'id_order': newItem.id_order,
            'description': product.description,
            'price': newItem.price,
            'quantity': newItem.quantity,
            'datetime': newItem.datetime
        })
    
    def removeItem(self, id_product, id_order):

        session = Session()
        itemToRemove = session.query(OrderItemAdapter).filter_by(id_order=id_order, id_product=id_product).first()
        orderToUpdate = session.query(OrderAdapter).filter_by(id_order=id_order).first()

        if orderToUpdate == None:
        
            return abort(404, 'Order with id %s does not exists' % id_order)
        
        elif itemToRemove == None:

            return abort(404, 'Product %s does not exists on order %s does not exists' % (id_product, id_order))

        elif orderToUpdate.order_status not in (1, 2):
        
            order_status = orderToUpdate.order_status
            order_status_description = self.order_status.get(order_status)
            return abort(423, 'You can not remove items on a order wich is %s' % (order_status_description))
        
        session.delete(itemToRemove)
        session.commit()

        return jsonify({
            'msg': 'Product %s removed from order with id %s' % (id_product, id_order)
            })