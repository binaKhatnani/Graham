# Graham
A simple pipeline to extract data from stock exchange websites, aggregate and analyse for insights.

## Current Working setup
- `pip install selenium`
- Download appropriate driver for [Chrome - click me](https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/)
- Place driver in root folder
- Create config.json in root folder with values as mentioned in next section but specific to your environment
- `pip install pandas`
- `pip install pyMongo`
- `pip install matplotlib`
- Setup MongoDB to listen to localhost on port 27107
- To run `python .\main.py`

## Config.json
- default values specified
```JSON
{ 
    "root": "Location to your Graham folder <No default, must be set manually>",
    "delete_files_after_processing": true, 
    "data_download": true,
    "data_process": true
}
```
- `root`: must specify the root location of the project
- `delete_files_after_processing`: deletes all files after processing
- `data_download`: determines if the download phase is executed which includes running selenium and downloading the files
- `data_process`: determines if the processing phase is executed which includes renaming file, parsing file and storing data in mongodb

## In development (Nice to have) setup
- `pip install scrapy`
- Use scrapy as alternative to fetching data from the web in a headless manner instead of selenium which runs the browser

## To Do
- [X] Setup selenium, load NSE homepage
- [X] Add links of pages where data can be extracted
- [X] Use selenium to download the files
- [X] Rename Downloaded files
- [X] Store processed data in MongoDB
- [ ] Implement UI to view data
- [ ] Run basic analytics or comparisons between data
- [ ] Add logging of operations so that failures or errors can be tracked (logger.py)
- [ ] Make it a 24/7 running application which initiates subprocess like a cron job

## Nice to have
- [ ] Implement intermediate language for scripting Selenium to download data
- [ ] Go headless which is possible by replacing selenium with scrapy or beautiful soup and perform data fetch 

