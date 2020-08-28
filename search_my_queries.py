import csv
import os
import requests
import urllib
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


queries = [
# insert your search terms here as strings ('') separating them with a comma
]

browser = webdriver.Chrome(r'c:/python/chromedriver/chromedriver.exe') # YOU WILL NEED TO INPUT THE PATH TO YOUR CHROMEDRIVER EXECUTABLE FILE IN THE FIRST ARGUMENT. WINDOWS OS MAY REQUIRE USING r BEFORE THE QUOTES AND PUTTING THE ACTUAL .EXE FILE IN THE PATH

### END CHROME DRIVER SETUP

browser.get('https://www.google.com')


for query in queries:
  elem = browser.find_element_by_name("q") #Find the input field to have Selenium type in the query
  elem.clear()
  elem.send_keys(query) #Selenium
  elem.send_keys(Keys.RETURN)
