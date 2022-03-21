import parcel_table
import adjacencymap
import truck
from datetime import time, datetime, date

# This function searches through the trucks to see if it has been assigned to a truck. If it has,
# it retrieves a report on that package through the truck. If not, it is still at the hub and only the package's
# information from the package table is retrieved. Worst case time complexity is O(n), where n is the number of
# trucks.
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
		return "Package " + str(p_id) + " is still at hub"
	return output


p_table = parcel_table.ParcelData()
admap = adjacencymap.MyAdjacencyMap()

truck1 = truck.Truck(1, admap, time(hour=8))
truck2 = truck.Truck(2, admap, time(hour=8))
truck3 = truck.Truck(3, admap, time(hour=11))
# All packages are assigned manually to the three trucks.
truck1.add_parcel(p_table.parcel_table.lookup(13))
truck1.add_parcel(p_table.parcel_table.lookup(15))
truck1.add_parcel(p_table.parcel_table.lookup(19))
truck1.add_parcel(p_table.parcel_table.lookup(14))
truck1.add_parcel(p_table.parcel_table.lookup(16))
truck1.add_parcel(p_table.parcel_table.lookup(27))
truck1.add_parcel(p_table.parcel_table.lookup(35))
truck1.add_parcel(p_table.parcel_table.lookup(39))
truck1.add_parcel(p_table.parcel_table.lookup(2))
truck1.add_parcel(p_table.parcel_table.lookup(33))
truck1.add_parcel(p_table.parcel_table.lookup(11))
truck1.add_parcel(p_table.parcel_table.lookup(17))
truck1.add_parcel(p_table.parcel_table.lookup(34))

truck2.add_parcel(p_table.parcel_table.lookup(3))
truck2.add_parcel(p_table.parcel_table.lookup(18))
truck2.add_parcel(p_table.parcel_table.lookup(36))
truck2.add_parcel(p_table.parcel_table.lookup(38))
truck2.add_parcel(p_table.parcel_table.lookup(37))
truck2.add_parcel(p_table.parcel_table.lookup(5))
truck2.add_parcel(p_table.parcel_table.lookup(7))
truck2.add_parcel(p_table.parcel_table.lookup(29))
truck2.add_parcel(p_table.parcel_table.lookup(20))
truck2.add_parcel(p_table.parcel_table.lookup(21))
truck2.add_parcel(p_table.parcel_table.lookup(4))
truck2.add_parcel(p_table.parcel_table.lookup(40))
truck2.add_parcel(p_table.parcel_table.lookup(24))
truck2.add_parcel(p_table.parcel_table.lookup(23))

truck3.add_parcel(p_table.parcel_table.lookup(6))
truck3.add_parcel(p_table.parcel_table.lookup(25))
truck3.add_parcel(p_table.parcel_table.lookup(28))
truck3.add_parcel(p_table.parcel_table.lookup(32))
truck3.add_parcel(p_table.parcel_table.lookup(9))
truck3.add_parcel(p_table.parcel_table.lookup(26))
truck3.add_parcel(p_table.parcel_table.lookup(8))
truck3.add_parcel(p_table.parcel_table.lookup(30))
truck3.add_parcel(p_table.parcel_table.lookup(31))
truck3.add_parcel(p_table.parcel_table.lookup(10))
truck3.add_parcel(p_table.parcel_table.lookup(22))
truck3.add_parcel(p_table.parcel_table.lookup(1))
truck3.add_parcel(p_table.parcel_table.lookup(12))

truck1.generate_path()
truck2.generate_path()
truck3.generate_path()

truck_list = [truck1, truck2, truck3]

# This function is used to get a report for all packages assigned to all trucks. Time complexity
# is O(n), where n is the total number of packages.
def all_package_report(truck_l):
	for truck in truck_l:
		print(truck.truck_report())

# The rest of this file implements the application UI.
quit = False
while not quit:
	print("Welcome to the WGUPS routing application. Choose one of the options below: ")
	print("    1. Report on all packages and truck driving distances.")
	print("    2. Report on specific packages at a specific time.")
	print("    3. Report on all packages at a certain time.")
	print("    4. Quit application")
	choice = int(input("Enter number 1-4 for your choice: "))
	print("Case = " + str(choice)) 
	match choice:
		case 1:
			all_package_report(truck_list)
			distance_sum = 0
			for t in truck_list:
				distance_sum += t.truck_distance_calc()

			print("All trucks together will have driven " + str(distance_sum) + " miles.")
		case 2:
			choice = int(input("Enter a package ID: "))
			valid_time = False
			time_in = None
			while not valid_time:
				time_in = input("Enter time in format HH:MM using 24 hour time: ")
				try:
					time_in = time.fromisoformat(time_in)
					valid_time = True
				except ValueError:
					print("Time entered is invalid. Please try again.")
			print(package_time_report(choice, time_in, truck_list, p_table, True))
		case 3:
			valid_time = False
			time_in = None
			while not valid_time:
				time_in = input("Enter time in format HH:MM using 24 hour time: ")
				try:
					time_in = time.fromisoformat(time_in)
					valid_time = True
				except ValueError:
					print("Time entered is invalid. Please try again.")
			for t in truck_list:
				for p in t.parcels:
					print(package_time_report(p, time_in, truck_list, p_table))
		case 4:
			print("Quitting...")
			quit = True
		case _:
			print("Input invalid. Please enter a valid choice.")

