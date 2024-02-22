class OrderEntity():
    # Meta Data
    table_name = 'orders'

    # Columns
    id_order = {'column_name': 'id_order', 'object_type': 'Column', 'data_type': 'Integer', 'primary_key': True}
    order_status = {'column_name': 'order_status', 'object_type': 'Column', 'data_type': 'Integer'}
    id_receipt = {'column_name': 'id_receipt', 'object_type': 'Column', 'data_type': 'Integer'}
    id_customer = {'column_name': 'id_customer', 'object_type': 'Column', 'data_type': 'Integer'}

    
    def getLenPrecision(column_name):

        try:
            lenght = int(0 if getattr(OrderEntity, column_name).get('length') == None else getattr(OrderEntity, column_name).get('length'))
            precision = int(0 if getattr(OrderEntity, column_name).get('precision') == None else getattr(OrderEntity, column_name).get('precision'))

            lenPrecision = '%s,%s' % (len, precision) if (precision != None and precision > 0) else len if precision != None else None

        except AttributeError as e:
            return type(e).__name__ + ': Column %s does not exists' % (e.name)
        
        return lenPrecision

    def getDataType(column_name):

        try:
            data_type = getattr(OrderEntity, column_name).get('data_type')

        except AttributeError as e:
            return type(e).__name__ + ': Column %s does not exists' % (e.name)
        
        return data_type
    
    def columnIsPK(column_name):
    
        try:
            primary_key = getattr(OrderEntity, column_name).get('primary_key')

        except AttributeError as e:
            return type(e).__name__ + ': Column %s does not exists' % (e.name)

        return False if primary_key == None else primary_key