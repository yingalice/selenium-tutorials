from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.twitch.tv/bbytesizedd/videos')

# Explicit wait will wait until the expected condition is met or give timeout exception
wait = WebDriverWait(driver, 5)
preferences = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-a-target="consent-banner-manage-preferences"]')))
preferences.click()

opt_out_checkbox = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'tw-checkbox__input')))
driver.execute_script('arguments[0].click()', opt_out_checkbox)

save = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Save Changes"]')))
save.click()

# On a Chrome browser launched by Selenium:
#   The privacy consent banner doesn't go away after setting preferences (also tried clicking manually)
#   Only works on a manually launched Chrome browser
#   Maybe it's a bot prevention measure
banner = wait.until(EC.invisibility_of_element((By.CLASS_NAME, 'consent-banner')))

driver.quit()