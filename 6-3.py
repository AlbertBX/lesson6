from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
#weiter = WebDriverWait (driver, 30)

pictures = WebDriverWait (driver, 10).until(EC.presence_of_element_located ((By.CSS_SELECTOR, '#image-container.col-12.py-2')))
img = driver.find_elements(By.ID, '#award')
#'img[src="img/award.png"]'


print(img.get_attribute('src'))

driver.quit()