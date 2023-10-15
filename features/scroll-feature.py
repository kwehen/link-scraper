from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import sensitive
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# Web Driver for Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Get Linkedin login page
driver.get("https://linkedin.com/uas/login")
time.sleep(3)

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
time.sleep(2)
search2 = driver.find_element(By.XPATH, "//input[@aria-label='City, state, or zip code']")
driver.execute_script("arguments[0].click();", search2)
# search2 = driver.find_element(By.CLASS_NAME, "jobs-search-box__ghost-text-input")
city = "Detroit, Michigan, United States"
search2.send_keys(city)
time.sleep(1)
search.send_keys(u'\ue007')
time.sleep(3)

job_links = []

jobs_block = driver.find_element(By.CLASS_NAME, "jobs-search-results-list")
jobs_list = jobs_block.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")

for job in jobs_list:
    driver.execute_script("arguments[0].scrollIntoView();", job)
    all_links = job.find_elements(By.TAG_NAME, 'a')
    for a in all_links:
        if str(a.get_attribute('href')).startswith("https://www.linkedin.com/jobs/view") and a.get_attribute('href') not in job_links: 
            job_links.append(a.get_attribute('href'))
        else:
            pass



print(job_links)
