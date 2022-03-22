import csv

class Hub:
	def __init__(self, name):
		self.name = name
		self.adjacencies = {}

	def __str__(self):
		output = ""
		for hub in self.adjacencies:
			output += hub + ": "
			output += str(self.adjacencies[hub]) + "\n"
		return output

class MyAdjacencyMap:
	def __init__(self):
		self.backing = {}
		with open('WGUPSDistanceTable.csv') as map_data:
			map_reader = csv.reader(map_data, dialect='excel')
			rows = list(map_reader)
			for hub in rows[1:]:
				new_hub = Hub(hub[1])
				for i in range(2, len(hub)):
					new_hub.adjacencies[rows[0][i]] = float(hub[i])
				self.backing[new_hub.name] = new_hub
			# labels = {}
			# i = 2
			# for hub in rows[0][2:]:
			# 	labels[i] = hub
			# 	i += 1
			# for hub in rows[1:]:
			# 	new_hub = Hub(hub[0])
			# 	for i in range(2,len(hub[2:])):
			# 		new_hub.adjacencies[labels[i]] = hub[i]
			# 	self.backing[new_hub.name] = new_hub

	def __str__(self):
		output = ""
		for hub in self.backing:
			output += self.backing[hub].name + "\n"
		return output

	def get_distance_to_from(self, origin, destination):
		distance = self.backing[origin].adjacencies[destination]
		return distance

if __name__ == "__main__":
    my_map = MyAdjacencyMap()
    # print(my_map)
    print(my_map.backing["HUB"])
    print(my_map.backing["HUB"].adjacencies["1488 4800 S"])
    print(my_map.get_distance_to_from("HUB", "4300 S 1300 E"))