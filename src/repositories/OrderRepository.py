from ..adapters.OrderAdapter import OrderAdapter
from ..services.CustomerService import CustomerService
from ..resources.dbconfig import Session
from flask import abort, jsonify
from requests import status_codes


class OrderRepository():

    def createOrder(document=''):
        session = Session()
        try:
            id_customer = '' if status_codes == 404 else CustomerService.getIdByDocument(document).id_customer

            newOrder = OrderAdapter(order_status=1, id_customer=id_customer)
            session.add(newOrder)
            session.commit()

            openedOrder = {
                        'msg': 'New order opened',
                        'id_order': newOrder.id_order,
                        'id_customer': newOrder.id_customer,
                        'order_status': newOrder.order_status,
                        }

            return jsonify(openedOrder)
        
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