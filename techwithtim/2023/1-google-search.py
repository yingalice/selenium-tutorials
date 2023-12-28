from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://google.com')

# Google search for 'tech with tim'
input_element = WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[title="Search"]'))
)
input_element.clear()
input_element.send_keys('tech with tim' + Keys.ENTER)

# Get all search results text containing 'Tech With Tim'
links = WebDriverWait(driver, 5).until(
  EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, 'Tech With Tim'))
)
for idx, link in enumerate(links):
  print(str(idx + 1) + ': ' + link.text + '\n')

driver.quit()