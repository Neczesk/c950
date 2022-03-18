from parcels import Parcel

class HashEntry:
	def __init__(self):
		self.items = []
		self.number = -1
	def __str__(self):
		output = "item: "
		for i in self.items:
			output += str(i.package_id)
		return output

class MyHashTable:
	def __init__(self, size):
		self.buckets = []
		self.table_size = size
		for i in range(size):
			self.buckets.append(HashEntry())
			self.buckets[-1].number = i
	def __str__(self):
		output = ""
		for bucket in self.buckets:
			output += "Bucket " + str(bucket.number) + ": " + str(bucket) + "\n"
		return output

	def insert(self, package):
		if isinstance(package, Parcel):
			bucket_num = package.package_id % self.table_size
			self.buckets[bucket_num].items.append(package)

	def lookup(self, key):
		bucket_num = key % self.table_size
		current_bucket = self.buckets[bucket_num]
		for item in current_bucket.items:
			if item.package_id == key:
				return item
		return None




