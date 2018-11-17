# Make a parcel list available to a class
parcels = []

#Implement a class so as to call from as an object later
class Parcel():
	def __init__(self):

		self.parcels = parcels

	def create(self, parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, user_id):
		order = {
			'parcel_id' : len(self.parcels) + 1,
			'parcel_name' 	: parcel_name,
			'parcel_weight' : parcel_weight,
			'pick_location' : pick_location,
			'destination' 	: destination,
			'consignee_name' : consignee_name,
			'consignee_no' 	: consignee_no,
			'order_status' : 'In Transit',
            'user_id' : user_id
		}

		self.parcels.append(order)
		return self.parcels

	# get all parcels
	def getParcels(self):
	    return self.parcels

	#get one parcel
	def getParcel(self, parcel_id):
		for parcel in self.parcels:
			if parcel['parcel_id'] == parcel_id:
				return parcel

	
	#cancel order status
	def cancelParcel(self, parcel_id):
		for parcel in self.parcels:
			if parcel['parcel_id'] == parcel_id:
				parcel['order_status'] = "Cancelled"
				return self.getParcel(parcel_id)

	#get users parcels
	def getUserParcels(self, user_id):
		userparcels = []
		for parcel in self.parcels:
			if parcel['user_id'] == user_id:
				userparcels.append(parcel)
		
		return userparcels



