from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://coursera.org')
driver.maximize_window()

logo = driver.find_element(By.CLASS_NAME, 'rc-CourseraLogo')
# print(logo.screenshot("C:/Users/Alice/Downloads/foo.png"))

driver.quit()