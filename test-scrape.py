from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import sensitive

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://linkedin.com/uas/login")
time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys(sensitive.username)
password = driver.find_element(By.ID, "password")
password.send_keys(sensitive.password)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

# driver = webdriver.Firefox("/Applications/Firefox.app")