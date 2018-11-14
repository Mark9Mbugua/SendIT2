# Make a parcel list available to a class
parcels = []

#Implement a class so as to call from as an object later
class Parcel():
	def __init__(self):

		self.parcels = parcels

	def hold(self, parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, user_id):
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
	def getparcels(self):
	    return self.parcels

	#get one parcel
	def getparcel(self, parcel_id):
		for parcel in self.parcels:
			if parcel['parcel_id'] == parcel_id:
				return parcel

	

	def cancelparcel(self, parcel_id):
		for parcel in self.parcels:
			if parcel['parcel_id'] == parcel_id:
				parcel['order_status'] = "Cancelled"
				return self.getparcel(parcel_id)

	#get users parcel
	def getuserparcels(self, user_id):
		pass



