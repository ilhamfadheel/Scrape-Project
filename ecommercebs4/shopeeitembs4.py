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
shopee_product = 'Kelly-Bag-Woven-Handbag-i.13865618.7839526734' 
shopee_product2= 'Tas-Serut-Polos-Hitam-Anti-Air-TSP001-M2W-i.443985.1901824878'
shopee_product3= 'Old-School-Sepatu-Converse-Old-Sneakers-Olahraga-Sepatu-Pria-Wanita-i.234869233.7360433341'
base_url = f'https://shopee.co.id/{shopee_product2}'

# set chrome driver options to disable any popup's from the website
# to find local path for chrome profile, open chrome browser
# and in the address bar type, "chrome://version"
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument("--headless")
# windows userdatadir path 'user-data-dir=C:\\Users\\username\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
#chrome_options.add_argument("user-data-dir=C:\\Users\\username\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
# To disable the message, "Chrome is being controlled by automated test software"
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# Pass the argument 1 to allow and 2 to block
chrome_options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
    })
# invoke the webdriver (MIND THE CHROMEDRIVER FILE according to your OS)
# windows dir path  r"..\chromedriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path = r"../chromedriver/chromedriver",
                          options = chrome_options)
browser.get(base_url)
delay = 5 #seconds

#----------- create table below

# declare empty lists
item_title, item_price, item_description = [], [], []
item_link, item_brand, item_stock = [],[],[]

while True:
    try:
        WebDriverWait(browser, delay)
        print (f"Page {base_url} is ready to be scraped")
        sleep(5)
        html = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        #print(html)
        soup = bs(html, "html.parser")

        # find_all() returns an array of elements. 
        # We have to go through all of them and select that one you are need. And than call get_text()
        
        item_parent_title = soup.find('div', attrs={'class': 'qaNIZv'}).find("span").text
        item_description.append(soup.find('div', attrs={'class': '_2u0jt9'}).find("span").text)
        item_link.append(base_url)
        item_brand.append(soup.find('a', attrs={'class': '_2H-513'}).get_text())


        item_combination_divs = soup.find('div', class_='_3a2wD-').find("div")

        #find the combination len of products ex. size,color
        combination_len = len(item_combination_divs)
        if combination_len <=3:
            combination_len+=1
        item_combination = [ [] for _ in range(combination_len-2) ]

        #find the combination name for the products ex. product name + size + color
        for n in range (combination_len - 2):
            item_combination_div = item_combination_divs.find_all("div")[n+1]
            for item_c in item_combination_div.find_all("button"):
                item_combination[n].append(item_c.get_text())

        if combination_len > 3:
            for n in range (len(item_combination[0])):
                #max [0] 5
                for m in range (len(item_combination[1])):
                    #max [1] 8
                    item_title.append(item_parent_title + ' ' + item_combination[0][n] + ' ' + item_combination[1][m])
        else:
            for n in range (len(item_combination[0])):
                item_title.append(item_parent_title + ' ' + item_combination[0][n])
        
        #find the price and stock for each variation
        

        print (item_title)
        print (item_description)
        print (item_brand)
        print (item_link)
        print (item_price)
        print (item_stock)

        break # it will break from the loop once the specific element will be present. 
    except TimeoutException:
        print ("Loading took too much time!-Try again")

#rows = zip(item_title, item_price, item_description, item_link, item_brand, item_stock)
#for row in rows:
#    print(row)


#import csv
#newFilePath = f'shopee_{shopee_product}_item_list.csv'
#with open(newFilePath, "wb") as myfile:
#    writer = csv.writer(myfile)
#    for row in rows:
#        writer.writerow(row)

# close the automated browser
browser.close()