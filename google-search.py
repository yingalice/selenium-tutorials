from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://www.google.com/'
query = 'test'

driver = webdriver.Chrome()
driver.get(url)

search = driver.find_element(By.NAME, 'q')
search.send_keys('Hello')
search.clear()
search.send_keys(query)
search.send_keys(Keys.RETURN)

# Search google for 'test', and return the titles of each result
try:
  results = WebDriverWait(driver, timeout = 5).until(lambda d : driver.find_elements(By.CSS_SELECTOR, '#search h3'))
  print('Title: ' + driver.title)
  print('SEARCH RESULTS')
  for idx, result in enumerate(results):
    print(str(idx) + ' - ' + result.text)
except Exception as e:
  print('Error: ' + str(type(e).__name__))
  driver.quit()