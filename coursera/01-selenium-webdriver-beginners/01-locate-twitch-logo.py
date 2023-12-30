from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://twitch.tv')

# Can set breakpoint and use debugger to find properties that will 
# validate your element (ie. accessible_name)
logo = driver.find_element(By.CLASS_NAME, 'tw-link')
print(logo.accessible_name)

driver.quit()