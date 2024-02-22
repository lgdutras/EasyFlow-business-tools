from ..adapters.CustomerAdapter import CustomerAdapter
from ..resources.dbconfig import Session
from flask import jsonify, abort

class CustomerRepository():

    def findCustomerByDocument(document):

        session = Session()   
        customer_query = session.query(CustomerAdapter).filter_by(document=document).first()
        
        if customer_query == None:

            return abort(404, 'None customer found with the provided document')

        else:

            customer_data = jsonify({
                'id_customer': customer_query.id_customer,
                'first_name': customer_query.first_name,
                'last_name': customer_query.last_name,
                'address': customer_query.address,
                'phone_number': customer_query.phone_number,
                'document': customer_query.document,
                'birthdate': customer_query.birthdate
            })

            return customer_data