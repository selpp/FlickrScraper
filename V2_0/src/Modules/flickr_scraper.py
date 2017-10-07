# flickr_scraper.py

# Dependencies
import json
import flickrapi
from time import sleep
from tqdm import tqdm
from base.scraper import Scraper

# The FlickrScraper class which inherits from Scraper
class FlickrScraper(Scraper):

	def __init__(self, per_page, api_config_file_path):
		Scraper.__init__(self, 'flickr')
		self.per_page = per_page
		self.flickr = self.init_api(api_config_file_path)
		print('[Flickr] Initialized!')

	def scrap_images(self, search, mysql_db_manager, label, max_page=None):
		pages = self.get_pages(search)

		for page in tqdm(xrange(1, pages + 1)):
			if max_page is not None and page > max_page:
				print('[Flickr] Reached max page!')
				return

			self.get_page_images(
				search,
				page,
				mysql_db_manager,
				label
			)

	def init_api(self, api_config_file_path):
		with open(api_config_file_path) as config_file:
			data = json.load(config_file)
			
			key = data['key']
			secret = data['secret']
			
			flickr = flickrapi.FlickrAPI(key, secret, format='parsed-json')
			return(flickr)

	def get_pages(self, search):
		pages = 0

		try:
			json_resp = self.flickr.photos.search(
					text = search,
					per_page = self.per_page,
					page = 1
				)
			pages = json_resp['photos']['pages']
		except Exception as e:
			print(e)

		sleep(1)

		print('[Flickr] Per Page: %s, Pages: %s' % (str(self.per_page), str(pages)))
		return(pages)

	def get_page_images(self, search, page, mysql_db_manager, label):
		try:
			json_resp = self.flickr.photos.search(
				text = search,
				per_page = self.per_page,
				page = page
			)
			images_data = json_resp['photos']['photo']

			for image_data in images_data:
				farm = image_data['farm']
				server = image_data['server']
				image_id = image_data['id']
				secret = image_data['secret']

				image_url = self.get_image_url(
					farm,
					server,
					image_id,
					secret
				)

				mysql_db_manager.add_image(self.name, label, image_url)
			mysql_db_manager.commit()
		except Exception as e:
			print('[Flickr] Failed getting images page: %s' % (str(page)))
			print(e)

		sleep(1)

	def get_image_url(self, farm, server, image_id, secret):
		url = "https://farm" + str(farm)
		url += ".staticflickr.com/" + str(server)
		url += "/" + str(image_id)
		url += "_" + str(secret)
		url += ".jpg"

		return(url)