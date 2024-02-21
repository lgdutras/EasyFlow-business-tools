from ..domain.customers.Customer import CustomerEntity
from sqlalchemy import Column, Integer, String, DECIMAL, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base

planb_database = declarative_base()

class CustomerAdapter(planb_database):

    def setDataType(column_name):

        dtypeAdapter = {'Integer': Integer, #Pass no precision cause Integer takes no arguments
                        'String': String(CustomerEntity.getLenPrecision(column_name)),
                        'Float': DECIMAL(CustomerEntity.getLenPrecision(column_name)),
                        'Date': Date(),
                        'Date_Time': DateTime()
                        }
        
        dtype = CustomerEntity.getDataType(column_name)

        if dtype in dtypeAdapter:
            return dtypeAdapter[dtype]
        else:
            raise ValueError(f"Unsupported data type: {dtype}")
    
    def setIsPK(column_name):
        return CustomerEntity.columnIsPK(column_name)

    __tablename__ = CustomerEntity.table_name
    id_customer = Column(setDataType('id_customer'), primary_key=setIsPK('id_customer'))
    first_name = Column(setDataType('first_name'), primary_key=setIsPK('first_name'))
    last_name = Column(setDataType('last_name'), primary_key=setIsPK('last_name'))
    address = Column(setDataType('address'), primary_key=setIsPK('address'))
    document = Column(setDataType('document'), primary_key=setIsPK('document'))
    phone_number = Column(setDataType('phone_number'), primary_key=setIsPK('phone_number'))
    birthdate = Column(setDataType('birthdate'), primary_key=setIsPK('birthdate'))