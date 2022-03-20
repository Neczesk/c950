import parcel_table
import adjacencymap
import truck
from datetime import time, datetime, date


def package_time_report(p_id, p_time, truck_list, p_table, show_package_info = False):
	relevant_truck = None
	output = ""
	if show_package_info:
		output += str(p_table.parcel_table.lookup(p_id)) + "\n"
	for truck in truck_list:
		if truck.is_parcel_on_truck(p_id):
			relevant_truck = truck
			break
	if relevant_truck != None and datetime.combine(date.today(), relevant_truck.start_time) < datetime.combine(date.today(), p_time):
		output += relevant_truck.package_time_report(p_id, p_time)
	else:
		return "Package is still at hub"
	return output


p_table = parcel_table.ParcelData()
admap = adjacencymap.MyAdjacencyMap()

truck1 = truck.Truck(1, admap, time(hour=8))
truck2 = truck.Truck(2, admap, time(hour=8))
truck3 = truck.Truck(3, admap, time(hour=12))

truck1.add_parcel(p_table.parcel_table.lookup(1))
truck1.add_parcel(p_table.parcel_table.lookup(2))
truck1.add_parcel(p_table.parcel_table.lookup(3))
truck1.add_parcel(p_table.parcel_table.lookup(4))
truck1.add_parcel(p_table.parcel_table.lookup(5))
truck1.add_parcel(p_table.parcel_table.lookup(6))
truck1.add_parcel(p_table.parcel_table.lookup(7))
truck1.add_parcel(p_table.parcel_table.lookup(8))
truck1.add_parcel(p_table.parcel_table.lookup(9))
truck1.add_parcel(p_table.parcel_table.lookup(10))
truck1.add_parcel(p_table.parcel_table.lookup(11))
truck1.add_parcel(p_table.parcel_table.lookup(12))
truck1.add_parcel(p_table.parcel_table.lookup(13))
truck1.generate_path()
truck2.add_parcel(p_table.parcel_table.lookup(14))
truck2.add_parcel(p_table.parcel_table.lookup(15))
truck2.add_parcel(p_table.parcel_table.lookup(16))
truck2.add_parcel(p_table.parcel_table.lookup(17))
truck2.add_parcel(p_table.parcel_table.lookup(18))
truck2.add_parcel(p_table.parcel_table.lookup(19))
truck2.add_parcel(p_table.parcel_table.lookup(20))
truck2.add_parcel(p_table.parcel_table.lookup(21))
truck2.add_parcel(p_table.parcel_table.lookup(22))
truck2.add_parcel(p_table.parcel_table.lookup(23))
truck2.add_parcel(p_table.parcel_table.lookup(24))
truck2.add_parcel(p_table.parcel_table.lookup(25))
truck2.add_parcel(p_table.parcel_table.lookup(26))
truck2.add_parcel(p_table.parcel_table.lookup(27))
truck2.generate_path()
truck3.add_parcel(p_table.parcel_table.lookup(28))
truck3.add_parcel(p_table.parcel_table.lookup(29))
truck3.add_parcel(p_table.parcel_table.lookup(30))
truck3.add_parcel(p_table.parcel_table.lookup(31))
truck3.add_parcel(p_table.parcel_table.lookup(32))
truck3.add_parcel(p_table.parcel_table.lookup(33))
truck3.add_parcel(p_table.parcel_table.lookup(34))
truck3.add_parcel(p_table.parcel_table.lookup(35))
truck3.add_parcel(p_table.parcel_table.lookup(36))
truck3.add_parcel(p_table.parcel_table.lookup(37))
truck3.add_parcel(p_table.parcel_table.lookup(38))
truck3.add_parcel(p_table.parcel_table.lookup(39))
truck3.add_parcel(p_table.parcel_table.lookup(40))
truck3.generate_path()

truck_list = [truck1, truck2, truck3]

for truck in truck_list:
	print(truck.truck_report())

print(package_time_report(23, time.fromisoformat("08:24"), truck_list, p_table, True))

# test_input = None
# valid_input = False
# while not valid_input:
# 	time_input = input("Enter time in format HH:MM using 24 hour time with no AM/PM indicator: ")
# 	try:
# 		test_time = time.fromisoformat(time_input)
# 		valid_input = True
# 	except ValueError:
# 		print("Time entered was invalid. Please try again.")

# print(test_time)
# print(package_time_report(13, test_time, truck_list))
