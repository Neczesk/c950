import parcel_table
import adjacencymap
import truck
from datetime import time

def package_time_report(p_id, p_time, truck_list):
	relevant_truck = None
	for truck in truck_list:
		if truck.is_parcel_on_truck(p_id):
			relevant_truck = truck
			break
	output = truck.package_time_report(p_id, p_time)
	return output

p_table = parcel_table.ParcelData()
admap = adjacencymap.MyAdjacencyMap()

truck1 = truck.Truck(1, admap, time(hour=8))
truck2 = truck.Truck(2, admap, time(hour=8))
truck3 = truck.Truck(3, admap, time(hour=12))

truck1.add_parcel(p_table.parcel_table.lookup(13))
truck1.generate_path()
truck_list = [truck1, truck2, truck3]

t = time(hour=9, minute=23)
print(package_time_report(13, t, truck_list))