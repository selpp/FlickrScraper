# Dependencies
import json
import flickrapi
import sys
from tqdm import *
from time import sleep

# Function to save a dictionnary into a json file
# {'name': , 'url': } -> {'name': , 'url': }
def dict_to_json(dictionnary, json_path):
	data = {}
	data['image'] = []

	for d in dictionnary:
		data['image'].append({
			'name': d['name'],
			'url': d['url']
		})

	try:
		with open(json_path, 'w') as outfile:
			json.dump(data, outfile, indent=4)
	except:
		print('[Error] Failed to save the file ...')
		sys.exit(2)

# Function to build the url and name for each image
# From a json file (response of the request)
# resp -> [{'name': , 'url': }]
# https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
# Need also the search text
def json_resp_to_dict(resp, search_text):
	images_data = []

	n = len(resp)
	for i in range(0, n):
		url = "https://farm" + str(resp[i]['farm'])
		url += ".staticflickr.com/" + str(resp[i]['server'])
		url += "/" + str(resp[i]['id'])
		url += "_" + str(resp[i]['secret'])
		url += ".jpg"

		name = search_text.replace(" ", "_") + "_"
		name += str(resp[i]['server']) + "_"
		name += str(resp[i]['id'])

		images_data.append({'name': name, 'url': url})
	return(images_data)

# Function to initialize the Flickr API
# Return a flickr object
# Need the json file with contain the key and the secret
def initialize_flickr_API(key_file_path):
	key_file_data = open(key_file_path)
	key_file = json.load(key_file_data)

	key = key_file['Key']
	secret = key_file['Secret']

	return(flickrapi.FlickrAPI(key, secret, format='parsed-json'))

# Function to search images on Flickr by text
# Return a dictionary of all images found
# resp -> [{'name': , 'url': }]
# Perform the search
# Opitional : license=2 -> Open-Source
def search_on_flickr(flickr, search_text, per_page):
	images_json = []
	page_number = 0
	images_infos = []

	# Get page infos
	images_json = flickr.photos.search(text=search_text, per_page=per_page, page=1)
	page_number = images_json['photos']['pages']
	print("[Info] Per page: " + str(per_page))
	print("[Info] Pages: " + str(page_number))
	images_json = []

	# Construct urls for each image
	# Get fileNames
	images_data = []

	# Perform the search for other pages
	for page in tqdm(range(1, page_number + 1)):
		sleep(1)

		try:
			images_json = flickr.photos.search(text=search_text, per_page=per_page, page=page)
			images_infos = images_json['photos']['photo']
			images_d = json_resp_to_dict(images_infos, search_text)
			images_data += images_d
		except:
			a = 0

	return(images_data)