# Scrape Project
This is an e-commerce web scraping project using python scrapy/beautifulsoup aimed to get products data/information including prices, stock, imageslink , etc.. into a downloadable csv/xlsx format. 
Which then can be uploaded to your/user's online shop or save it for yourself if you just want to get the targeted store's products information. This Project is aimed to be a dropshipping app.

status: in-progress
https://scrape.sorudeshop.com/

## Get started by cloning the repo and installing python virtual env

1. Clone to your local machine

2. install venv using python3

`python3 -m venv venv`

3. run venv 

on windows cmdprompt run `source venv/Scripts/activate.bat`

4. install scrapy and beautifulsoup inside the venv

`pip3 install scrapy`

`pip3 install beautifulsoup4`

5.  a. Look for related scripts inside ecomercescrapy/spiders if using scrapy

ex. `scrapy crawl shopee`
    b. Run python script if usiing beautifulsoup4
