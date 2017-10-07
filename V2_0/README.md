# TIDMARSH ImagesScraper V2.0

## What's new ?
* New implementation
* Cleaner version
* Easier to add others search api in the future (Modules folder)

## Current Version APIs:
* Flickr API

## What for ?
* Scrap images on the web based on a search tag(text).
* Will be used to populate a dataset for the CNN trainning

## How to use ?
* Past your Key and Secret you've earned from the Flickr API Web Services into a FlickrAPIConfig.json file
* FlickrAPIConfig.json File and place it into src/APIKeys/:
```json
{
	"key": "................................",
	"secret": "................"
}
```
* Past your DataBase infos into a MySqlConfig.json file
* MySqlConfig.json File and place it into src/APIKeys/:
```json
{
	"host": "---.---.---.---",
	"user": "------",
	"password": "--------",
	"db": "--------"
}```
* Run a terminal
* Run the config file to install all dependencies
```
sudo bash config.sh
```
* Run the script scraper_exec.py in src/ wtih all the parameters: search label
```
python3 scraper_exec.py --search=car --label=0
```
* Let the script do the work
* It will add the images urls into the database

## Output data ?
* Saved into a MySql data base
id | local_path | status | scraper | class | url