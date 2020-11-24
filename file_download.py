import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.facebook.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
open('facebook.ico', 'wb').write(r.content)

browser = webdriver.Chrome("chromedriver")


