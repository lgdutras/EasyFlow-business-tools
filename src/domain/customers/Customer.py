class CustomerEntity():
    # Meta Data
    table_name = 'customers'

    # Columns
    id_customer = {'column_name': 'id_customer', 'object_type': 'Column', 'data_type': 'Integer', 'primary_key': True}
    first_name = {'column_name': 'first_name', 'object_type': 'Column', 'data_type': 'String', 'length': '45'}
    last_name = {'column_name': 'last_name', 'object_type': 'Column', 'data_type': 'String', 'length': '45'}
    address = {'column_name': 'address', 'object_type': 'Column', 'data_type': 'String', 'length': '150'}
    document = {'column_name': 'document', 'object_type': 'Column', 'data_type': 'String', 'length': '11'}
    phone_number = {'column_name': 'phone_number', 'object_type': 'Column', 'data_type': 'String', 'length': '12'}
    birthdate = {'column_name': 'birthdate', 'object_type': 'Column', 'data_type': 'String', 'length': '45'}

    
    def getLenPrecision(column_name):

        try:
            lenght = int(0 if getattr(CustomerEntity, column_name).get('length') == None else getattr(CustomerEntity, column_name).get('length'))
            precision = int(0 if getattr(CustomerEntity, column_name).get('precision') == None else getattr(CustomerEntity, column_name).get('precision'))

            lenPrecision = '%s,%s' % (len, precision) if (precision != None and precision > 0) else len if precision != None else None

        except AttributeError as e:
            return type(e).__name__ + ': Column %s does not exists' % (e.name)
        
        return lenPrecision

    def getDataType(column_name):

        try:
            data_type = getattr(CustomerEntity, column_name).get('data_type')

        except AttributeError as e:
            return type(e).__name__ + ': Column %s does not exists' % (e.name)
        
        return data_type
    
    def columnIsPK(column_name):
    
        try:
            primary_key = getattr(CustomerEntity, column_name).get('primary_key')

        except AttributeError as e:
            return type(e).__name__ + ': Column %s does not exists' % (e.name)

        return False if primary_key == None else primary_key