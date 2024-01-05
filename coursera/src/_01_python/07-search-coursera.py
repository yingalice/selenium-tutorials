from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://coursera.org')
wait = WebDriverWait(driver, 15)

# Search coursera.org for 'Influencer Marketing', and print the search results
search_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'react-autosuggest__input')))
search_input.click()
search_input.send_keys('Influencer Marketing' + Keys.ENTER)  # Could not click 0 size magnifying glass button, had to press Enter

results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h3.cds-CommonCard-title')))
for result in results:
  print(result.text)

driver.quit()