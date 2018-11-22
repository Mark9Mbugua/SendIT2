from ....db_config import init_db


class Parcel():

    def __init__(self):
        self.db = init_db()

    def serializer(self, parcel):
        parcel_fields = ('parcel_name', 'parcel_weight', 'pick_location',
                         'destination', 'consignee_name', 'consignee_no', 'order_status', 'cost', 'user_id')
        result = dict()
        for index, field in enumerate(parcel_fields):
            result[field] = parcel[index]
        return result

    def create(self, parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost):
        cur = self.db.cursor()
        query = """INSERT INTO parcels (parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost, user_id)
                VALUES (%s, %s, %s, %s,%s, %s,%s, %s)"""
        content = (parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost)
        cur.execute(query, content)
        self.db.commit()
        self.db.close()
        return self.serializer(content)

    def getParcels(self):
        cur = self.db.cursor()
        query = """SELECT parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost FROM parcels"""
        cur.execute(query)
        data = cur.fetchall()
        return self.serializer(data)

    def getParcel(self, parcel_id):
        cur = self.db.cursor()
        query = """SELECT parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost
        FROM parcels WHERE parcel_id = %s""", (parcel_id, )
        cur.execute(query)
        data = cur.fetchall()
        return self.serializer(data)
