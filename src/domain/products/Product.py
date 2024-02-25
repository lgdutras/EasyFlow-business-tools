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

class ProductEntity(Entity):

    # Meta Data
    table_name = 'products'

    # Columns
    id_product = {'column_name': 'id_product', 'object_type': 'Column', 'data_type': 'Integer', 'primary_key': True}
    description = {'column_name': 'description', 'object_type': 'Column', 'data_type': 'String', 'length': '45'}
    cost = {'column_name': 'cost', 'object_type': 'Column', 'data_type': 'Decimal', 'length': '8', 'precision': '4'}
    price = {'column_name': 'price', 'object_type': 'Column', 'data_type': 'Decimal', 'length': '8', 'precision': '4'}
    id_recipe = {'column_name': 'description', 'object_type': 'Column', 'data_type': 'String', 'length': '5'}
    product_type = {'column_name': 'product_type', 'object_type': 'Column', 'data_type': 'String', 'length': '45'}
