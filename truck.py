import adjacencymap
from datetime import datetime, time, date, timedelta

def sort_tuples_by_distance(t):
	return t[1]

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

	def generate_path(self):
		#This is where pathfinding takes place. I'm using a nearest neighbor algorithm
		self.path.clear()
		remaining_parcels = self.parcels.copy()
		current_location = self.start_location
		for i in range(0, len(self.parcels)):
			closest_package_tuple = self.get_closest_parcel_id(current_location, remaining_parcels)
			self.path.append(closest_package_tuple)
			remaining_parcels.pop(closest_package_tuple[0])
			current_location = self.parcels[closest_package_tuple[0]].delivery_address


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

	def formatted_packaged_report(self, parcel_id, parcel_tuple):
		output = "Parcel " + str(parcel_id) + " will be delivered at: "
		output += str(parcel_tuple[0]) + ".\n"
		output += "The truck will have driven " + str(parcel_tuple[1]) + " miles."
		return output

	def time_report(self, report_time):
		current_time = datetime.combine(date.today(), self.start_time)
		for i in range(0, len(self.path())):
			next_package_info = self.package_report(self.path[i])
			if (next_package_info[0] > report_time):
				break #If the next package delivery time is greater than the report time, that is the package currently being delivered at the given time
			else:
				pass #calculate a new current time and distance then try the next package. The report should say which package is currently being delivered

	def truck_report(self):
		pass




if __name__ == "__main__":
	import parcel_table
	p_table = parcel_table.ParcelData()
	t = Truck(0, adjacencymap.MyAdjacencyMap(), time(hour=8))
	t.add_parcel(p_table.parcel_table.lookup(4))
	t.add_parcel(p_table.parcel_table.lookup(7))
	t.add_parcel(p_table.parcel_table.lookup(13))
	t.generate_path()
	print(t.path)
	print(t.formatted_packaged_report(13, t.package_report(13)))