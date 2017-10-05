# Dependencies
from utils import *

# Print Header
print('===========================================')
print('===========                   =============')
print('===========   FlickrScraper   =============')
print('===========                   =============')
print('=============================  V 1.0  =====')
print('===========================================\n')

def flickr_search(search_text, json_file_path):
	# Initiate the API with the key and the secret
	flickr = initialize_flickr_API("Flickr/Key.json")

	# Number of images per request
	per_page = 500

	# Get the images data
	images_data = search_on_flickr(flickr, search_text, per_page)

	# Print info
	print "[Output] Images Found: " + str(len(images_data))

	# Write the images data into a json file
	if(len(images_data) > 0):
		json_filename = 'Results/' + json_file_path + '.json'
		dict_to_json(images_data, json_filename)
	else:
		print('[Output] The research dose not have any images related to ...')

	print('\n')
	print('===========================================\n')
