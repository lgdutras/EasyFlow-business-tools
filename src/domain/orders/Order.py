class Entity():

    def getLenPrecision(self, column_name):

        try:
            length = int(0 if getattr(self, column_name).get('length') == None else getattr(self, column_name).get('length'))
            precision = int(0 if getattr(self, column_name).get('precision') == None else getattr(self, column_name).get('precision'))

            lenPrecision = '%s,%s' % (len, precision) if (precision != None and precision > 0) else len if precision != None else None

        except AttributeError as e:
            return type(e).__name__ + ': Column %s does not exists' % (e.name)
        
        return lenPrecision

    def getDataType(self, column_name):

        try:
            data_type = getattr(self, column_name).get('data_type')

        except AttributeError as e:
            return type(e).__name__ + ': Column %s does not exists' % (e.name)
        
        return data_type
    
    def columnIsPK(self, column_name):
    
        try:
            primary_key = getattr(self, column_name).get('primary_key')

        except AttributeError as e:
            return type(e).__name__ + ': Column %s does not exists' % (e.name)

        return False if primary_key == None else primary_key

class OrderEntity(Entity):

    # Meta Data
    table_name = 'orders'

    # Columns
    id_order = {'column_name': 'id_order', 'object_type': 'Column', 'data_type': 'Integer', 'primary_key': True}
    order_status = {'column_name': 'order_status', 'object_type': 'Column', 'data_type': 'Integer'}
    id_receipt = {'column_name': 'id_receipt', 'object_type': 'Column', 'data_type': 'Integer'}
    id_customer = {'column_name': 'id_customer', 'object_type': 'Column', 'data_type': 'Integer'}
    

class OrderItemEntity(Entity):

    # Meta Data
    table_name = 'order_product'

    # Columns
    id_order = {'column_name': 'id_order', 'object_type': 'Column', 'data_type': 'Integer', 'primary_key': True}
    id_product = {'column_name': 'id_product', 'object_type': 'Column', 'data_type': 'Integer'}
    price = {'column_name': 'price', 'object_type': 'Column', 'data_type': 'Decimal', 'length': '8', 'precision': '4'}
    quantity = {'column_name': 'quantity', 'object_type': 'Column', 'data_type': 'Integer'}
    datetime = {'column_name': 'datetime', 'object_type': 'Column', 'data_type': 'Datetime'}
