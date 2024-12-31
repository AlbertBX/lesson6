from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")
blue_button = driver.find_elements(By.ID, 'ajaxButton')

blue_button = WebDriverWait (driver, 10).until(EC.element_to_be_clickable ((By.CSS_SELECTOR, 'button[class="btn btn-primary"]')))
  
blue_button.click()


green_message = WebDriverWait (driver, 16).until(EC.visibility_of_element_located ((By.CLASS_NAME, "bg-success")))
print(green_message.text)
driver.quit()