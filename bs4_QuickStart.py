import requests
from bs4 import BeautifulSoup

r = requests.get('https://w3schools.com/python/demopage.htm')
soup = BeautifulSoup(r.content, 'html.parser')

#-----------------------------------------------------------------#
#selenium quick start 1


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


ser = Service("PATH")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get(url)
# r = driver.page_source #page source
# soup = BeautifulSoup(r, 'html.parser') #access by bs4


#-----------------------------------------------------------------#
#selenium quick start 2

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
