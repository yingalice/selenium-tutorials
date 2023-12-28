from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker/')

cookie_id = 'bigCookie'
cookies_id = 'cookies'
product_prefix = 'product'
product_price_prefix = 'productPrice'

# Select English language
language = WebDriverWait(driver, 5).until(
  EC.element_to_be_clickable((By.XPATH, '//*[text()="English"]'))
)
language.click()

# Wait for load screen to disappear
WebDriverWait(driver, 5).until(
  EC.invisibility_of_element_located((By.ID, 'loading'))
)

# Look for cookie count
retry_limit = 2
for retry_count in range(retry_limit):
  try:
    cookie = WebDriverWait(driver, 5).until(
      EC.element_to_be_clickable((By.ID, cookie_id))
    )
    break
  except StaleElementReferenceException:
    if retry_count == retry_limit - 1:
      raise

# Play game: Click on cookie, buy upgrades as they become available 
while True:
  # Remove commas, causes issues in python
  cookie.click()
  cookies_count = int(driver.find_element(By.ID, cookies_id).text.split(' ')[0].replace(',', ''))

  for i in range(4):
    # If price is not a digit (ie. '???'), skip to next product
    try:
      product_price = int(driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(',', ''))
    except ValueError:
      continue
    if cookies_count >= product_price:
      product = driver.find_element(By.ID, product_prefix + str(i))
      product.click()
      break