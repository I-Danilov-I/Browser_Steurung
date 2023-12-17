from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Erstelle ChromeOptions für Konfigurationsoptionen des Chrome-Browsers
options = ChromeOptions()

# Setze die Option, um das Browserfenster maximiert zu starten
options.add_argument("--start-maximized")

# Erstelle den WebDriver mit dem ChromeDriverManager
driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Gehe zur Wikipedia-Seite
driver.get("https://www.wikipedia.de")

# Warte 10 Sekunden, um sicherzustellen, dass die Seite vollständig geladen ist
time.sleep(10)

# Finde das Suchfeld (nach ID) und gebe den Suchbegriff "Salzburg" ein
search_bar = driver.find_element(By.ID, 'txtSearch')
search_bar.send_keys('Salzburg')

# Finde den Suchbutton (nach ID) und klicke darauf
button = driver.find_element(By.ID, 'cmdSearch')
button.click()

# Warte auf die Ergebnisseite und extrahiere den Artikeltext (nach ID)
article_element = driver.find_element(By.ID, 'content')
article_text = article_element.text

# Gib den Artikeltext aus
print(article_text)

# Warte 1000 Sekunden (16 Minuten)
time.sleep(1000)

# Beende den WebDriver
driver.quit()

