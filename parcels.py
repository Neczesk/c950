
class Parcel:
	def __init__(self):
		package_id = -1
		delivery_address = ""
		delivery_deadline = ""
		delivery_city = ""
		delivery_zip_code = ""
		package_weight = -1
		delivery_status = "At Hub"
		special_note = ""
	def __str__(self):
		output = ""
		output += "Package ID: " + str(self.package_id) + "\n"
		output += "Delivery Address: " + str(self.delivery_address) + "\n"
		output += "Delivery Deadline: " + str(self.delivery_deadline) + "\n"
		output += "Delivery City: " + str(self.delivery_city) + "\n"
		output += "Delivery Zip Code: " + str(self.delivery_zip_code) + "\n"
		output += "Package Weight: " + str(self.package_weight) + "\n" 
		output += "Delivery Status: " + str(self.delivery_status) + "\n"
		output += "Special Note: " + str(self.special_note) + "\n"
		return output



