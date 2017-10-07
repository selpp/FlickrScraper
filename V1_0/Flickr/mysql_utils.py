# Dependencies
import pymysql
import json

# Function to connect to the Mysql db
# Return the connection and the cursor
def connect(database_file_path):
	database_connection_data = open(database_file_path)
	database_connection_file = json.load(database_connection_data)

	host = database_connection_file['host']
	user = database_connection_file['user']
	password = database_connection_file['password']
	db = database_connection_file['db']

	connection = pymysql.connect(host=host, user=user, password=password, db=db)
	cursor = connection.cursor()
	return(connection, cursor)

# Function to add an image to the db
# Given the scraper name, the label, the url,
# the curso and the connection
def insert_image(scraper, label, remote_path, cursor, connection):
	sql_add = 'INSERT INTO Image_Test (scraper, status, class, remote_path) VALUES (%s, %s, %s, %s)'
	sql_values = ('flickr', 0, label, remote_path)
	try:
		cursor.execute(sql_add, sql_values)
		connection.commit()
	except:
		print('[Error] Image can not be added to the DB (already in certainly) ...')

# Debug Function to show the db
def show_images(cursor):
	sql_show = "SELECT * FROM Image_Test"
	cursor.execute(sql_show)
	rows = cursor.fetchall()
	for row in rows:
		print(row)

# Function to stop the session
def deconnect(connection):
	connection.close()