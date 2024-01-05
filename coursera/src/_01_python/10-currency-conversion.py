from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime

driver = webdriver.Chrome()
driver.get('https://wise.com/gb/compare')
wait = WebDriverWait(driver, 5)

def get_clickable_element(*locator):
  try:
    return wait.until(EC.element_to_be_clickable((locator)))
  except TimeoutException as e:
    print(type(e).__name__ + str(locator))

# Select from currency: USD
get_clickable_element(By.XPATH, '(//button[contains(@class, "btn")])[1]').click()
get_clickable_element(By.CSS_SELECTOR, '#option--USD > a').click()

# Select to currency: INR
get_clickable_element(By.XPATH, '(//button[contains(@class, "btn")])[2]').click()
get_clickable_element(By.CSS_SELECTOR, '#option--INR > a').click()

# Type 5000 in amount field
amount = get_clickable_element(By.CSS_SELECTOR, 'div.tw-money-input > input')
amount.click()
amount.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)  # amount.clear() didn't work
amount.send_keys('5000')

# Tell user if USD -> INR conversion is favorable or not
target_rupees = 415000
result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table>tbody>tr>td:last-child>span')))
rupees = float(result.text.split(' ')[0].replace(',', ''))
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
if (rupees > target_rupees):
  print(timestamp + ': YAY!  Exchange rate IS favorable!  5,000 USD for ' + result.text)
else:
  print(timestamp + ': AWW!  Exchange rate is NOT favorable!  5,000 USD for ' + result.text)

driver.quit()