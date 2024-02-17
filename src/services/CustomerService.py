from ..repositories.CustomerRepository import CustomerRepository
from flask import jsonify


class CustomerService(CustomerRepository):

    def findCustomerByDocument(document):
        
        return CustomerRepository.findCustomerByDocument(document)