import scrapy
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep

class ShopeeSpider(scrapy.Spider):
    name = "shopee_spider"
    allowed_domains = ['shopee.co.id']
    shop_name="aldmond22"
    start_urls = [f'http://shopee.co.id/{shop_name}']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('disable-notifications')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('start-maximized')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('user-data-dir=C:\\Users\\Nayla Syafa\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        chrome_options.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 2
        })
        self.driver = webdriver.Chrome(executable_path = '../chromedriver/chromedriver.exe', options = chrome_options)

    def parse(self, response):
        self.driver.get(response.url)
        self.delay = 5 