from parcels import Parcel

# The HashEntry class is used as the bucket for my implementation of a hash table.
# It tracks how many items are in the bucket and which index the bucket has in the
# overall table.
class HashEntry:
	def __init__(self):
		self.items = []
		self.number = -1
	def __str__(self):
		output = "item: "
		for i in self.items:
			output += str(i.package_id)
		return output
# My hash table implementation uses linear chaining to resolve hash collisions.
# When the table is constructed it is given the number of parcels it will be containing,
# which allows the table to be appropriately sized. It also affects the hash function;
# if the table is constructed with the correct size there should be no hash collisions, as
# because the hash function uses a modulo operation with the table size as an operand in 
# order to give each entry a unique hash.
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
			# The hash function uses the table size. If the table size is set to the
			# number of packages, this produces a unique hash for each package.
			bucket_num = package.package_id % self.table_size
			self.buckets[bucket_num].items.append(package)

	def lookup(self, key):
		bucket_num = key % self.table_size
		current_bucket = self.buckets[bucket_num]
		for item in current_bucket.items:
			if item.package_id == key:
				return item
		return None




