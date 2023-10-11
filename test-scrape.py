from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import sensitive
from selenium.webdriver.common.keys import Keys

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
time.sleep(1)
search.send_keys(u'\ue007')
time.sleep(3)

# Get the links for each job displayed
job_links = []
job_title = driver.find_elements(By.CLASS_NAME, "job-card-container__link")
for job in job_title:
    link = job.get_attribute("href")
    # Open link in new tab
    driver.execute_script("window.open('" + link + "');")
    time.sleep(0.5)
    job_links.append(link)

# Next step is to scroll the page and add more jobs to the list + open them
# Additional step is to go to each page and scrape the job description/requirements
tab = 1
num = len(job_links)

file = open("job_descriptions.txt", "w")

while tab <= num:
    driver.switch_to.window(driver.window_handles[tab])
    time.sleep(3)
    see_more = driver.find_element(By.XPATH, "//button[@aria-label='Click to see more description']")
    see_more.click()
    description = driver.find_element(By.ID, "job-details")
    file.write(f'\nJob {tab}\n {description.text}')
    print(f"Job {tab} of {num} scraped successfully")
    time.sleep(2)
    tab += 1

file.close()
driver.quit()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.quit()