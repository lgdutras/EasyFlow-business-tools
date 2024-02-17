from sqlalchemy import Column, Integer, String, DECIMAL, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base

planb_database = declarative_base()

class CustomerEntity(planb_database):
    __tablename__ = 'customers'
    id_customer = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    address = Column(String(150))
    document = Column(String(11))
    phone_number = Column(String(12))
    birthdate = Column(String(45))
