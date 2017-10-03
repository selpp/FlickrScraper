# ImagesScraper

## What for ?
* Scrap images from flickr and google based on a search tag(text).
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
* (It will be the same with google API when we will add it)
* Run a terminal
* Run the config file to install all dependencies
```
sudo bash config.sh
```
* Run the script wtih all the parameters: scraper name (flickr or google) search_text and json_file_name
```
python3 MainScraper.py flickr car car

python3 MainScraper.py google car car
```
* Let the script do the work
* The file will be created in the Results folder so make sure to have one in this repo

## Output data ?
* Json file
```json
{
	{
		"name": "imagename1",
		"url": "http://urlimage1"
	}

	.
	.
	.

	{
		"name": "imagenameN",
		"url": "http://urlimageN"
	}
}
```