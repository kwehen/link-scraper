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

time.sleep(3)

jobs_link = driver.find_element(By.LINK_TEXT, "Jobs")
jobs_link.click()

time.sleep(3)

job_src = driver.page_source
soup = BeautifulSoup(job_src, 'lxml')

search = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
search.send_keys("Devops Engineer")
time.sleep(1)
search.send_keys(u'\ue007')