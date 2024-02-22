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
