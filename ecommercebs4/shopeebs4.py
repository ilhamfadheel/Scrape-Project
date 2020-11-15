import requests
from bs4 import BeautifulSoup as bs

r=requests.get("https://shopee.co.id/aldmond22")

soup = bs(r.content)

print(soup)