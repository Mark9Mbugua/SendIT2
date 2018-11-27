from ....db_config import init_db
import itertools
import psycopg2


class Parcel():

    def __init__(self):
        self.db = init_db()

    def serializer(self, parcel):
        parcel_fields = ('parcel_id','parcel_name', 'parcel_weight', 'pick_location',
                         'destination', 'consignee_name', 'consignee_no', 'order_status', 'cost', 'user_id')
        result = dict()
        print(parcel)
        for index, field in enumerate(parcel_fields):
            result[field] = parcel[index]
        return result

    def create(self, parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost, user_id):
        cur = self.db.cursor()
        query = """INSERT INTO parcels (parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost, user_id)
                VALUES (%s, %s, %s, %s,%s, %s,%s, %s, %s) RETURNING parcel_id"""
        content = (parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost, user_id)
        cur.execute(query, content)
        parcel_id = cur.fetchone()
        self.db.commit()
        cur.close()
        return self.serializer(tuple(itertools.chain(parcel_id, content)))

    def getAllParcels(self):
        cur = self.db.cursor()
        query = """SELECT parcel_id, parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost, user_id FROM parcels"""
        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        return self.serializer(data)
        

    def getOneParcel(self, parcel_id):
        cur = self.db.cursor()
        query = """SELECT parcel_id, parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost, user_id
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
        

    def changeParcelStatus(self, parcel_id, order_status):
        cur = self.db.cursor()
        cur.execute = ""
