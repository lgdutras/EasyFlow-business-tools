from ..domain.products.Product import ProductEntity
from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

planb_database = declarative_base()

class ProductAdapter(planb_database):

    def setDataType(column_name):

        dtypeAdapter = {'Integer': Integer, #Pass no precision cause Integer takes no arguments
                        'Decimal': DECIMAL,
                        'String': String,
                        }
        
        dtype = ProductEntity().getDataType(column_name)

        if dtype in dtypeAdapter:
            return dtypeAdapter[dtype]
        else:
            raise ValueError(f"Unsupported data type: {dtype}")
    
    def setIsPK(column_name):
        return ProductEntity().columnIsPK(column_name)
    
    __tablename__ = ProductEntity.table_name
    id_product = Column(setDataType('id_product'), primary_key=setIsPK('id_product'))
    description = Column(setDataType('description'), primary_key=setIsPK('description'))
    cost = Column(setDataType('cost'), primary_key=setIsPK('cost'))
    price = Column(setDataType('price'), primary_key=setIsPK('price'))
    id_recipe = Column(setDataType('id_recipe'), primary_key=setIsPK('id_recipe'))
    product_type = Column(setDataType('product_type'), primary_key=setIsPK('product_type'))
