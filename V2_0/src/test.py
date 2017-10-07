# test.py

# Dependencies
from DataBase.mysql_db import MySqlSession
from Modules.flickr_scraper import FlickrScraper

database = MySqlSession('APIKeys/MySqlConfig.json', 'Image_Test')

flickr_scraper = FlickrScraper(1, 'APIKeys/FlickrAPIConfig.json')
flickr_scraper.scrap_images('eye', database, 0, max_page = 2)

database.disconnect()