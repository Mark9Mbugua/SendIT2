# Make a parcel list available to a class
parcels = []

#Implement a class so as to call from as an object later
class Parcel():
	def __init__(self):

		self.parcels = parcels

	def hold(self, parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, user_id):
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
		pass

	#get one parcel
	def getparcel(self, parcel_id):
		pass

	

	def cancelparcel(self, parcel_id):
		pass

	#get users parcel
	def getuserparcels(self, user_id):
		pass



