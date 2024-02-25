from ..domain.orders.Order import OrderEntity, OrderItemEntity
from sqlalchemy import Column, Integer, DECIMAL, DateTime
from sqlalchemy.ext.declarative import declarative_base

planb_database = declarative_base()

class OrderAdapter(planb_database):

    def setDataType(column_name):

        dtypeAdapter = {
                        'Integer': Integer, #Pass no precision cause Integer takes no arguments
                        }

        dtype = OrderEntity().getDataType(column_name)

        if dtype in dtypeAdapter:
            return dtypeAdapter[dtype]
        else:
            raise ValueError(f"Unsupported data type: {dtype}")
    
    def setIsPK(column_name):
        return OrderEntity().columnIsPK(column_name = column_name)

    __tablename__ = OrderEntity.table_name
    id_order = Column(setDataType('id_order'), primary_key=setIsPK('id_order'))
    order_status = Column(setDataType('order_status'), primary_key=setIsPK('order_status'))
    id_receipt = Column(setDataType('id_receipt'), primary_key=setIsPK('id_receipt'))
    id_customer = Column(setDataType('id_customer'), primary_key=setIsPK('id_customer'))

class OrderItemAdapter(planb_database):

    def setDataType(column_name):

        dtypeAdapter = {'Integer': Integer, #Pass no precision cause Integer takes no arguments
                        'Decimal': DECIMAL,
                        'Datetime': DateTime,
                        }
        
        dtype = OrderItemEntity().getDataType(column_name)

        if dtype in dtypeAdapter:
            return dtypeAdapter[dtype]
        else:
            raise ValueError(f"Unsupported data type: {dtype}")
     
    def setIsPK(column_name):
        return OrderItemEntity().columnIsPK(column_name)

    __tablename__ = OrderItemEntity.table_name
    id_order = Column(setDataType('id_order'), primary_key=setIsPK('id_order'))
    id_product = Column(setDataType('id_product'), primary_key=setIsPK('id_product'))
    price = Column(setDataType('price'), primary_key=setIsPK('price'))
    quantity = Column(setDataType('quantity'), primary_key=setIsPK('quantity'))
    datetime = Column(setDataType('datetime'), primary_key=setIsPK('datetime'), autoincrement=True)