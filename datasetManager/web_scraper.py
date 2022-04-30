#Using Selenium for web scraping
from selenium import webdriver

#Instead of manually downloading, unzipping and adding the chromedriver to path, use the manager package
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Start browser with Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://google.com')

