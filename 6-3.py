from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 100)

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')



images=WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#image-container.col-12.py-2 img#landscape")))
img = driver.find_elements(By.CSS_SELECTOR, '#award')

print(len(images))

src = images(2).get_attribute("src")

print(src)

driver.quit()
