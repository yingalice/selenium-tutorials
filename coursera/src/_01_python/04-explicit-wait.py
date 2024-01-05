from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get('https://www.twitch.tv/bbytesizedd/videos')

# Explicit wait will wait until the expected condition is met or give timeout exception
try:
  wait = WebDriverWait(driver, 2)
  cookies = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.tw-image')))
  print(cookies.tag_name)
except TimeoutException as e:
  print(type(e).__name__)

driver.quit()