from ..domain.customers.Customer import CustomerEntity
from ..resources.dbconfig import Session
from flask import jsonify

class CustomerRepository():

    def findCustomerByDocument(document):

        session = Session()
        customer_query = session.query(CustomerEntity).filter_by(document=document).first()
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