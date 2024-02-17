from ..services.CustomerService import CustomerService
from flask import request
from flask_restful import Resource

class CustomerController(Resource):

    def get(self):
        
        return CustomerService.findCustomerByDocument(request.args.get('document'))