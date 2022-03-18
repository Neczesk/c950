import parcel_table
import adjacencymap
import truck
from datetime import time, datetime, date


def package_time_report(p_id, p_time, truck_list):
	relevant_truck = None
	for truck in truck_list:
		if truck.is_parcel_on_truck(p_id):
			relevant_truck = truck
			break
	if relevant_truck != None and datetime.combine(date.today(), relevant_truck.start_time) < datetime.combine(date.today(), p_time):
		output = relevant_truck.package_time_report(p_id, p_time)
	else:
		return "Package is still at hub"
	return output

p_table = parcel_table.ParcelData()
admap = adjacencymap.MyAdjacencyMap()

truck1 = truck.Truck(1, admap, time(hour=8))
truck2 = truck.Truck(2, admap, time(hour=8))
truck3 = truck.Truck(3, admap, time(hour=12))

truck1.add_parcel(p_table.parcel_table.lookup(13))
truck1.generate_path()
truck3.add_parcel(p_table.parcel_table.lookup(27))
truck_list = [truck1, truck2, truck3]

t = time(hour=9, minute=23)
print(package_time_report(13, t, truck_list))
print(package_time_report(27, t, truck_list))
test_time = time.fromisoformat("08:00")
print(test_time)
