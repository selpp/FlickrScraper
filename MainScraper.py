# Dependencies
import sys
sys.path.insert(0, 'Flickr/')
from FlickrScraper import *

# Error exit function
def exit_error():
	print('[Error] Argument errors, should be : python MainScraper flickr/google search_text label')
	print('[Error] use example: python MainScraper flickr car 0')
	print('\n')
	print('===========================================\n')
	sys.exit(2)

# Main method call search function
def main(argv):
	scrapers = ['flickr', 'google']

	if len(argv) < 3:
		exit_error()
	elif argv[0] not in scrapers:
		exit_error()

	if argv[0] == 'flickr':
		flickr_search(argv[1], argv[0], argv[2])

if __name__ == "__main__":
	main(sys.argv[1:])
