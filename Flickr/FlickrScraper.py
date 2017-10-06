# Dependencies
from utils import *
from mysql_utils import *

# Print Header
print('===========================================')
print('===========                   =============')
print('===========   FlickrScraper   =============')
print('===========                   =============')
print('=============================  V 1.0  =====')
print('===========================================\n')

def flickr_search(search_text, scraper, label):
	# Initiate the API with the key and the secret
	flickr = initialize_flickr_API("Flickr/Key.json")

	# Number of images per request
	per_page = 1#500

	# Get the images data
	images_data = search_on_flickr(flickr, search_text, per_page)

	# Print info
	print("[Output] Images Found: " + str(len(images_data)))

	# Write the images data into the DB
	if(len(images_data) > 0):
		# Connct to the DB
		(connection, cursor) = connect("Flickr/Database.json")
		# Add to the DB
		dict_to_db(scraper, label, images_data, cursor, connection)
		# Close the connection
		deconnect(connection)

		print('[Output] The images hav been correcctly added to the DB!')
	else:
		print('[Output] The research dose not have any images related to ...')

	print('\n')
	print('===========================================\n')
