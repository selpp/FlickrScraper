# ImagesScraper

## What for ?
* Scrap images from flickr and google based on a search tag(text).
* Will be used to populate a dataset for the CNN trainning

## How to use ?
* Past your Key and Secret you've earned from the Flickr API Web Services into a Key.json file
* Key.json File and place it into the Flickr Folder:
```json
{
	"Key": "................................",
	"Secret": "................"
}
```
* (It will be the same with google API when we will add it)
* Past your DataBase infos into a Database.json file
* Database.json File and place it into the Flickr Folder:
```json
{
	"host": "---.---.---.---",
	"user": "------",
	"password": "--------",
	"db": "--------"
}
* Run a terminal
* Run the config file to install all dependencies
```
sudo bash config.sh
```
* Run the script wtih all the parameters: scraper name (flickr or google) search_text and label_index
```
python3 MainScraper.py flickr car 0

python3 MainScraper.py google car 0
```
* Let the script do the work
* The file will be created in the Results folder so make sure to have one in this repo

## Output data ?
* Save into a data base
id | local_path | status | scraper | class | url