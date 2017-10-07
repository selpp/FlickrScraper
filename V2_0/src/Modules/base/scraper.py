# scraper.py

# An implementation of the base Scraper class
class Scraper(object):

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return("I am a %s scraper!" % (self.name))

	def scrap_images(self, search, mysql_db_manager):
		pass