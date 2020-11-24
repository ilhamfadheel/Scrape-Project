import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep

# create object for chrome options
chrome_options = Options()
#future update will make variable below to be a pass on call argument
shopee_merchant= 'aldmond22'
base_url = f'https://shopee.co.id/{shopee_merchant}'

# set chrome driver options to disable any popup's from the website
# to find local path for chrome profile, open chrome browser
# and in the address bar type, "chrome://version"
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('start-maximized')
#mind the directory below to point to your chrome's profile 'user-data-dir=C:\\Users\\username\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
chrome_options.add_argument("user-data-dir=C:\\Users\\Nayla Syafa\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
# To disable the message, "Chrome is being controlled by automated test software"
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# Pass the argument 1 to allow and 2 to block
chrome_options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
    })
# invoke the webdriver (MIND THE CHROMEDRIVER FILE according to your OS)
browser = webdriver.Chrome(executable_path = r"..\chromedriver\chromedriver.exe",
                          options = chrome_options)
browser.get(base_url)
delay = 5 #seconds

#----------- create table below

# declare empty lists
item_cost, item_init_cost, item_loc = [],[],[]
item_name, items_sold, discount_percent = [], [], []
while True:
    try:
        WebDriverWait(browser, delay)
        print ("Page is ready")
        sleep(5)
        html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        #print(html)
        soup = bs(html, "html.parser")
        #below is just for debugging total inside lists of each

        

        # find_all() returns an array of elements. 
        # We have to go through all of them and select that one you are need. And than call get_text()
        
        for item_n in soup.find_all('div', class_='_1NoI8_ _16BAGk'):

            print(item_n.get_text())
            item_name.append(item_n.text)

        # find the price of items
        for item_c in soup.find_all('span', class_='_341bF0'):

            print(item_c.get_text())
            item_cost.append(item_c.text)

        # find initial item cost
        for item_ic in soup.find_all('div', class_ = '_1w9jLI QbH7Ig U90Nhh'):

            print(item_ic.get_text())
            item_init_cost.append(item_ic.text)
        # find total number of items sold/month
        for items_s in soup.find_all('div',class_ = '_18SLBt'):

            print(items_s.get_text())
            items_sold.append(items_s.text)

        # find item discount percent
        for dp in soup.find_all('span', class_ = 'percent'):

            print(dp.get_text())
            discount_percent.append(dp.text)
        # find item location
        for il in soup.find_all('div', class_ = '_3amru2'):

            print(il.get_text())
            item_loc.append(il.text)

        break # it will break from the loop once the specific element will be present. 
    except TimeoutException:
        print ("Loading took too much time!-Try again")


rows = zip(item_cost, item_init_cost, item_loc, item_name, items_sold, discount_percent)
for row in rows:
    print(row)

# close the automated browser
browser.close()

#import csv
#newFilePath = f'shopee_{shopee_merchant}_item_list.csv'
#with open(newFilePath, "wb") as myfile:
#    writer = csv.writer(myfile)
#    for row in rows:
#        writer.writerow(row)

