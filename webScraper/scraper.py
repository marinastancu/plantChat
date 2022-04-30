#Using Selenium for web scraping
from selenium import webdriver
#Reading .env files for PATH
import os
from dotenv import load_dotenv

#Extract PATH from local config file
load_dotenv()
DRIVER_PATH = os.getenv('DRIVER_PATH')

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')