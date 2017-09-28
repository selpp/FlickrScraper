# FlickrScraper

## What for ?
* Scrap images from flickr based on a search tag(text).
* Will be used to populate a dataset for the CNN trainning

## How to use ?
* Past your Key and Secret you've earned from the Flickr API Web Services into a Key.json file
* Key.json File:
```json
{
	"Key": "................................",
    "Secret": "................"
}
```
* Run a terminal
* Run the config file to install all dependencies
```
sudo bash config.sh
```
* Run the script
```
python3 FlickrScraper.py
```
* Type the tag you want to search imahges for
* Let the script do the work
* Type the json file path (ex: cars.json for a car search)

## Output data ?
* Json file
```json
{
	{
		'name': 'imagename1',
		'url': 'http://urlimage1'
	}

	.
	.
	.

	{
		'name': 'imagenameN',
		'url': 'http://urlimageN'
	}
}
```