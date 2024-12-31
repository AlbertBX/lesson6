from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")
input_field = driver.find_element(By.ID,'newButtonName')

input_field.send_keys("ScyPro")

blue_button = driver.find_elements(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
blue_button = WebDriverWait (driver, 2).until(EC.element_to_be_clickable ((By.CSS_SELECTOR, 'button[class="btn btn-primary"]')))
  
blue_button.click()


blue_message = WebDriverWait (driver, 2).until(EC.visibility_of_element_located ((By.CSS_SELECTOR, 'button[class="btn btn-primary"]')))
print(blue_message.text)
driver.quit()