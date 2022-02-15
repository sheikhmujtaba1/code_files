from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

usernameStr = 'muhammad.mujtaba@centre.edu'
passwordStr = 'iloveAllah1_'

browser = webdriver.Chrome()
browser.get(('https://urldefense.com/v3/__https://centre.libstaffer.com/admin/home__;!!PFjsk5_m8oRWKtmR!eFMRb-UZQfTFX0a93daFFyY0EOpqFzFUb1hhU70voQaWCc9VkkE-g6dK5fAEc_ou2YW4KH3x$'))

username = browser.find_element_by_id('s-libapps-email')
username.send_keys(usernameStr)
password = browser.find_element_by_id('s-libapps-password')
password.send_keys(passwordStr)

time.sleep(1)
login_button = browser.find_element_by_id('s-libapps-login-button')
login_button.click()

time.sleep(5)
openshift = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'gutabc')))
openshift.click()


currentUrl = browser.current_url

print(currentUrl)

#login to libstaffer
status = requests.get(currentUrl, auth=(usernameStr, passwordStr))
#get html page
soup = BeautifulSoup(status.content, "html.parser")

print(soup)
##results = soup.find(class="sorting_1")
##print(results.prettify())





