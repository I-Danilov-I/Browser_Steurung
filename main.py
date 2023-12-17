from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = ChromeOptions()
options.add_argument("--start-maximized")

driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.wikipedia.de")
time.sleep(10)

search_bar = driver.find_element(By.ID, 'txtSearch')
search_bar.send_keys('Salzburg')

button = driver.find_element(By.ID, 'cmdSearch')
button.click()

article_element = driver.find_element(By.ID, 'content')
article_text = article_element.text
print(article_text)

time.sleep(1000)
driver.quit()
