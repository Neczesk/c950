import adjacencymap
from datetime import datetime, time, date, timedelta

# This is used to sort the packages for the pathfinding function. It sorts by the distance.
def sort_tuples_by_distance(t):
	return t[1]

# The Truck class holds the data for each truck, and contains the behavior needed for
# the efficient pathfinding.
class Truck:
	def __init__(self, id, nav_table, start_time):
		self.id = id
		self.driver = -1
		self.start_time = start_time
		self.path = []
		self.parcels = {}
		self.delivered_parcels = {}
		self.nav_table = nav_table
		self.start_location = "HUB"

	# This is where pathfinding takes place. I'm using a nearest neighbor algorithm to do this.
	# The truck finds the closest package to the hub and delivers that one, then finds the closest
	# package to that one, then continues on. The time complexity of this code is O(n^2 * logn) because the call
	# to get_closest_parcel_id is O(n*logn) and is contained by a loop that is also O(n).
	def generate_path(self):
		
		self.path.clear()
		remaining_parcels = self.parcels.copy()
		current_location = self.start_location
		for i in range(0, len(self.parcels)):
			closest_package_tuple = self.get_closest_parcel_id(current_location, remaining_parcels)
			self.path.append(closest_package_tuple)
			remaining_parcels.pop(closest_package_tuple[0])
			current_location = self.parcels[closest_package_tuple[0]].delivery_address

	# This finds the package id with the address closest to the truck's given location. The time complexity
	# is O(n*logn) to be more exact because the loop is O(n) and python's list sort algorithm is O(logn)
	def get_closest_parcel_id(self, origin, input_dict):
		distance_tuple_list = []
		for parcel in input_dict:
			distance = self.nav_table.get_distance_to_from(origin, self.parcels[parcel].delivery_address)
			distance_tuple_list.append((input_dict[parcel].package_id, distance))
		distance_tuple_list.sort(key=sort_tuples_by_distance)
		return distance_tuple_list[0]

	def add_parcel(self, parcel):
		self.parcels[parcel.package_id] = parcel
		# self.generate_path()

	# This gets a tuple that can be used to generate reports for the main application. It 
	# loops through the path (which must be generated first) and returns a tuple of the form
	# (time_delivered, distance_driven). Time complexity is O(n), with n being the number of
	# packages assigned to that truck.
	def package_report(self, parcel_id):
		#returns a tuple of the form (time_delivered, distance driven)
		output = ""
		if parcel_id in self.parcels:
			tracked_distance = 0
			elapsed_time = timedelta()
			for i in range(0, len(self.path)):
				next_id = self.path[i][0]
				next_stop_distance = self.path[i][1]
				tracked_distance += next_stop_distance
				elapsed_time = elapsed_time + timedelta(minutes=(next_stop_distance / 0.3))
				if next_id == parcel_id:
					break
		return (datetime.combine(date.today(), self.start_time) + elapsed_time, tracked_distance)

	# This function uses the tuple from package_report to generate a formatted string.
	def formatted_packaged_report(self, parcel_id, parcel_tuple):
		output = "Parcel " + str(parcel_id) + " will be delivered at: "
		output += str(parcel_tuple[0]) + ".\n"
		output += "The truck will have driven " + str(parcel_tuple[1]) + " miles."
		return output

	# Reports the status of the given package at the given time. It uses the package_report
	# tuple to see if a package has been delivered yet.
	def package_time_report(self, parcel_id, time) -> str:
		output = ""
		if parcel_id in self.parcels:
			p_tup = self.package_report(parcel_id)
			if datetime.combine(date.today(), time) < p_tup[0]:
				output += "Package " + str(parcel_id) + " has not yet been delivered"
			else:
				output += "Package " + str(parcel_id) + " was delivered at " + str(p_tup[0])
		return output

	def set_package_status(self, parcel_id, time):
		if parcel_id in self.parcels:
			p_tup = self.package_report(parcel_id)
			if datetime.combine(date.today(), time) < p_tup[0]:
				self.parcels[parcel_id].delivery_status = "en route"
			else:
				self.parcels[parcel_id].delivery_status = "delivered at " + str(p_tup[0]) + "."


	def truck_report(self) -> str:
		# returns a string indicating a delivery time for all packages 
		# assigned to the truck as well as total miles driven at the end.
		# Time complexity is O(n^2) because of the call to package_report, which is 
		# O(n)
		output = ""
		for parcel in self.parcels:
			pack_tuple = self.package_report(self.parcels[parcel].package_id)
			output += "Package " + str(self.parcels[parcel].package_id) + " will be delivered at: "
			output += str(pack_tuple[0]) + "\n"

		output += "The truck will have driven a total of " + str(self.truck_distance_calc()) + " miles."
		return output

	# Gets the total distance driven by the truck. Time complexity is O(n), where n is the number of parcels assigned to the truck.
	def truck_distance_calc(self) -> int:
		distance_sum = 0
		for parcel in self.path:
			distance_sum += parcel[1]
		return distance_sum

	def is_parcel_on_truck(self, id) -> bool:
		if id in self.parcels:
			return True
		else:
			return False



# This code is only for testing.
if __name__ == "__main__":
	import parcel_table
	p_table = parcel_table.ParcelData()
	t = Truck(0, adjacencymap.MyAdjacencyMap(), time(hour=8))
	t.add_parcel(p_table.parcel_table.lookup(4))
	t.add_parcel(p_table.parcel_table.lookup(7))
	t.add_parcel(p_table.parcel_table.lookup(13))
	t.generate_path()
	# print(t.path)
	# print(t.formatted_packaged_report(13, t.package_report(13)))
	print(t.truck_report())
	report_time = time(hour=8, minute = 10)
	report_time = datetime.combine(date.today(), report_time)
	print(t.package_time_report(7, report_time))