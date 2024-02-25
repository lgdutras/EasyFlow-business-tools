from ..adapters.ProductAdapter import ProductAdapter
from ..resources.dbconfig import Session
from flask import abort, jsonify


class ProductRepository():

    def getProductById(id_product):
        
        session = Session()
        product_data = session.query(ProductAdapter).filter_by(id_product = id_product).first()

        if product_data == None:

            return abort(404, 'None product found with the provided id')

        else:

            return product_data