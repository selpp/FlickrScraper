# Dependencies
import sys
from utils import *

# Print Header
print('===========================================')
print('===========                   =============')
print('===========   FlickrScraper   =============')
print('===========                   =============')
print('=============================  V 1.0  =====')
print('===========================================\n')

exit = False

while not exit:
	# Initiate the API with the key and the secret
	flickr = initialize_flickr_API("Key.json")

	# Get the user search input
	search_text = raw_input('[Input] Search: ')

	# Number of images per request
	per_page = 500

	# Get the images data
	images_data = search_on_flickr(flickr, search_text, per_page)

	# Print info
	print "[Output] Images Found: " + str(len(images_data))

	# Write the images data into a json file
	if(len(images_data) > 0):
		json_filename = raw_input('[Input] File name (Store the results): ')
		dict_to_json(images_data, json_filename)
	else:
		print('[Output] The research dose not have any images related to ...')

	exit_resp = raw_input('[Input] Do you want to quit ? y/Y or n/N: ')
	exit = (exit_resp == 'y' or exit_resp == 'Y')
	print('\n')
	print('===========================================\n')
	if exit:
		quit()