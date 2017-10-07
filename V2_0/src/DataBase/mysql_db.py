# mysql_db.py

# Dependencies
import pymysql
import json

# The MySql database class
class MySqlSession(object):

	def __init__(self, mysql_db_config_file_path, table_name):
		self.connection, self.cursor = self.connect(mysql_db_config_file_path)
		self.table_name = table_name
		print('[MySql] Connected!')

	def connect(self, mysql_db_config_file_path):
		with open(mysql_db_config_file_path) as config_file:
			data = json.load(config_file)
			
			host = data['host']
			user = data['user']
			password = data['password']
			db = data['db']

			connection = pymysql.connect(
				host = host,
				user = user,
				password = password,
				db = db
			)
			cursor = connection.cursor()
			return(connection, cursor)

	def disconnect(self):
		self.connection.close()
		print('[MySql] Disconnected!')

	def add_image(self, scraper_name, label, image_url):
		req = 'INSERT INTO '
		req += self.table_name
		req += ' (scraper, status, class, remote_path)'
		req += ' VALUES (%s, %s, %s, %s)'

		values = (scraper_name, 0, label, image_url)

		try:
			self.cursor.execute(req, values)
		except Exception as e:
			print('[MySql] Failed to add ...')
			print(e)

	def commit(self):
		try:
			self.connection.commit()
			print('[MySql] Commit!')
		except Exception as e:
			print('[MySql] Failed to commit ...')
			print(e)