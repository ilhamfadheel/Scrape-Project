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

on linux shell/bash run `source venv/bin/activate`

or you can also use Visual Studio Code python interpreter
     by pressing `ctrl + shift + p` and type python interpeter, and choose venv folder.

4. install the required python library inside the venv

`pip3 install scrapy` - might need to install wheel as dependency

`pip3 install beautifulsoup4`

`pip3 install selenium`

install the right version of chromedriver here `https://sites.google.com/a/chromium.org/chromedriver/downloads`

5.  a. Look for related scripts inside ecomercescrapy/spiders if using scrapy

ex. `scrapy crawl shopee`
    b. Run python script if usiing beautifulsoup4
