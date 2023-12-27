from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# Don't automatically close browser when script finishes
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.neuralnine.com')
driver.maximize_window()
wait = WebDriverWait(driver, 5)

# Click 'Books' link
link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[./span[contains(text(), "Books")]]')))
link.click()

# Click Amazon link that has H2 text of '7 in 1' (make sure ancestor div in question only has 2 links, to avoid returning results from an outer div)
book_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "elementor-column-wrap")][.//h2[text()[contains(., "7 IN 1")]]][count(.//a)=2]//a')))
book_link.click()

# Switch Selenium to 2nd tab (Amazon link)
driver.switch_to.window(driver.window_handles[1])

# Get the paperback price
# If unsuccessful, refresh page to retry.  Sometimes it says:
# "We're sorry, an error has occurred. Please reload this page and try again."
retry_limit = 2
for retry_count in range(retry_limit):
  try:
    button = driver.find_element(By.XPATH, '//a[.//span[text()="Paperback"]]//span[text()[contains(., "$")]]')
    print(button.get_attribute('innerHTML'))
    break
  except NoSuchElementException:
    driver.refresh()