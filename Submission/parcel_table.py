import parcels
import hash_table
import csv
import datetime

# The ParcelData class contains all the useful information that the application needs to keep track of.
# When constructed it opens the package_data.csv file as its information source and uses the Parcel class
# and my hash table implementation to store the data.
class ParcelData:
	def __init__(self):
		with open('package_data.csv') as parcel_data:
			parcel_reader = csv.reader(parcel_data, dialect='excel')
			rows = list(parcel_reader)
			self.parcel_table = hash_table.MyHashTable(len(rows))
			for row in rows[1:]:
				new_parcel = parcels.Parcel()
				new_parcel.package_id = int(row[0])
				new_parcel.delivery_address = row[1]
				new_parcel.delivery_city = row[2]
				new_parcel.delivery_zip_code = row[4]
				new_parcel.delivery_deadline = row[5]
				new_parcel.package_weight = int(row[6])
				new_parcel.delivery_status = "At hub"
				new_parcel.special_note = row[7]
				self.parcel_table.insert(new_parcel)