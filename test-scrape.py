from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import sensitive

# Web Driver for Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Get Linkedin login page
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

# Login
username = driver.find_element(By.ID, "username")
username.send_keys(sensitive.username)
password = driver.find_element(By.ID, "password")
password.send_keys(sensitive.password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for page to load
time.sleep(3)

# Go to the jobs page
jobs_link = driver.find_element(By.LINK_TEXT, "Jobs")
jobs_link.click()

# Wait for page to load
time.sleep(3)

# Search for specific job title
search = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
# In the future, change this to input variable so that a user can scrape for their specified job title
search.send_keys("Devops Engineer")
time.sleep(1)
search.send_keys(u'\ue007')