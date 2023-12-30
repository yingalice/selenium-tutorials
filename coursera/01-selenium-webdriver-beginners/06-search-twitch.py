from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://twitch.tv/directory/all')

# Search twitch.tv for 'glasses', and print the search results
wait = WebDriverWait(driver, 5)
input_search = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-a-target="tray-search-input"] input.tw-input')))
input_search.click()
input_search.send_keys('glasses' + Keys.ENTER)
results = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'strong')))
for result in results:
  print(result.text)

driver.quit()