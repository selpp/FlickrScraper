# Dependencies
import sys
from FlickrScraper import *

# Error exit function
def exit_error():
	print('[Error] Argument errors, should be : python MainScraper flickr/google search_text json_save_file_name')
	print('[Error] use example: python MainScraper flickr car car')
	print('\n')
	print('===========================================\n')
	sys.exit(2)

# Main method call search function
def main(argv):
	scrapers = ['flickr', 'goole']

	if len(argv) < 3:
		exit_error()
	elif argv[0] not in scrapers:
		exit_error()

	if argv[0] == 'flickr':
		flickr_search(str(argv[1]), 'Results/' + str(argv[2]) + '.json')

if __name__ == "__main__":
	main(sys.argv[1:])