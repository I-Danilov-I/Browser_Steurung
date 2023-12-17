from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

options = ChromeOptions()
options.add_argument("--start-maximized")

driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.youtube.com/")
time.sleep(10)
