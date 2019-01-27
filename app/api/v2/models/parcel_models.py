from ....db_config import init_db
import itertools
import psycopg2
import re


class Parcel():

    def __init__(self):
        self.db = init_db()

    def serializer(self, parcel):
        parcel_fields = ('parcel_id','parcel_name', 'parcel_weight', 'pick_location',
                         'destination', 'present_location', 'consignee_name', 'consignee_no', 'order_status', 'cost', 'user_id')
        result = dict()
        print(parcel)
        for index, field in enumerate(parcel_fields):
            result[field] = parcel[index]
        return result  
    
    def second_serializer(self, parcel_data):
        # coverting data retrived from the database into objects
        parcels = []
        for index, parcel_value in enumerate(parcel_data):
            parcel_id, parcel_name, parcel_weight, pick_location, destination, present_location, consignee_name, consignee_no, order_status, cost, user_id = parcel_value
            parcel = dict(parcel_id=parcel_id, parcel_name=parcel_name, parcel_weight=parcel_weight, pick_location=pick_location, destination=destination, 
                        present_location=present_location, consignee_name=consignee_name, consignee_no=consignee_no, order_status=order_status, cost=cost, user_id=user_id)
            parcels.append(parcel)
        
        return parcels


    def create(self, parcel_name, parcel_weight, pick_location, destination, present_location, consignee_name, consignee_no, order_status, cost, user_id):
        cur = self.db.cursor()
        query = """INSERT INTO parcels (parcel_name, parcel_weight, pick_location, destination, present_location, consignee_name, consignee_no, order_status, cost, user_id)
                VALUES (%s, %s, %s, %s,%s, %s,%s, %s, %s, %s) RETURNING parcel_id"""
        content = (parcel_name, parcel_weight, pick_location, destination, present_location, consignee_name, consignee_no, order_status, cost, user_id)
        cur.execute(query, content)
        parcel_id = cur.fetchone()
        self.db.commit()
        cur.close()
        return self.serializer(tuple(itertools.chain(parcel_id, content)))

    def getUserParcels(self, user_id):
        user_parcels = []
        cur = self.db.cursor()
        query = """SELECT parcel_id, parcel_name, parcel_weight, pick_location, destination, present_location, consignee_name, consignee_no, order_status, cost, user_id FROM parcels"""
        cur.execute(query)
        data = cur.fetchall()
        serial_data = self.second_serializer(data)
        print(serial_data)
        cur.close()
        for parcel in serial_data:
            if parcel['user_id'] == user_id:
                user_parcels.append(parcel)

        print(user_parcels)
        return user_parcels
    
    def validate_parcel_data(self, parcel_name, destination, consignee_name, pick_location, present_location, 
                                parcel_weight, consignee_no, order_status, cost, user_id):
        """validates parcel data"""
        response  = True

        if not re.search('^[A-Za-z]', parcel_name):
            response = "Parcel name should start with a capital letter"
            return response

        elif not re.search('^[A-Za-z]', destination):
            response = "Destination should start with a capital letter"
            return response
        
        elif not re.search('^[A-Za-z]', consignee_name):
            response = "Consignee's name should start with a capital letter"
            return response
        
        elif not re.search('^[A-Za-z]', pick_location):
            response = "Pick-up location name should start with a capital letter"
            return response

        elif not re.search('^[A-Za-z]', present_location):
            response = "Present location should start with a capital letter"
            return response

        elif not isinstance(cost, int):
            response = "Cost number must be an integer"
            return response

        elif not isinstance(parcel_weight, int):
            response = "Parcel weight must be an integer"
            return response
        
        elif not isinstance(consignee_no, int):
            response = "Consignee's number must be an integer"
            return response
        
        elif not isinstance(user_id, int):
            response = "User Id must be an integer"
            return response
        
        elif not isinstance(parcel_name, str):
            response = "Parcel number must be in letters"
            return response

        elif not isinstance(destination, str):
            response = "Consignee's number must be in letters"
            return response
        
        elif not isinstance(pick_location, str):
            response = "Pick-up location must be in letters"
            return response
        
        elif not isinstance(present_location, str):
            response = "Present location must be in letters"
            return response
        
        elif not isinstance(consignee_name, str):
            response = "Consignee's number must be in letters"
            return response
        
        elif not isinstance(order_status, str):
            response = "Order status must be in letters"
            return response

        return response

    def getOneParcel(self, parcel_id):
        cur = self.db.cursor()
        query = """SELECT parcel_id, parcel_name, parcel_weight, pick_location, destination, present_location, consignee_name, consignee_no, order_status, cost, user_id
        FROM parcels WHERE parcel_id = {}""".format(parcel_id)
        cur.execute(query)
        data = cur.fetchone()
        return self.serializer(data)

    #update destination
    def updateParcel(self, destination, parcel_id, user_id):
        cur = self.db.cursor()
        query = """UPDATE parcels SET destination = '{}' WHERE parcel_id = '{}' AND user_id = '{}' RETURNING destination""".format(destination, parcel_id, user_id)
        cur.execute(query)
        self.db.commit()
        dest = cur.fetchone()
        cur.close()
        destination = dest
        new_dest = dict(destination=destination)
        return new_dest
    
    def getAllParcels(self):
        cur = self.db.cursor()
        query = """SELECT parcel_id, parcel_name, parcel_weight, pick_location, destination, present_location, consignee_name, consignee_no, order_status, cost, user_id FROM parcels"""
        cur.execute(query)
        data = cur.fetchall()
        return self.second_serializer(data)
    
    def updateLocation(self, present_location, parcel_id, user_id):
        cur = self.db.cursor()
        query = """UPDATE parcels SET present_location = '{}' WHERE parcel_id = '{}' AND user_id  = '{}' RETURNING present_location""".format(present_location, parcel_id, user_id)
        cur.execute(query)
        self.db.commit()
        locale =  cur.fetchone()
        cur.close()
        location = locale
        new_location = dict(location = location)
        return new_location
    
    def updateOrderStatus(self, order_status, parcel_id, user_id):
        cur = self.db.cursor()
        query = """UPDATE parcels SET order_status = '{}' WHERE parcel_id = '{}' AND user_id = '{}' RETURNING order_status""".format(order_status, parcel_id, user_id)
        cur.execute(query)
        self.db.commit()
        status = cur.fetchone()
        cur.close()
        order_status = status
        new_status = dict(order_status=order_status)
        return new_status
    

        
