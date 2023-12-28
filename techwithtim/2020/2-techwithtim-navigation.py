from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
import traceback

driver = webdriver.Chrome()
driver.get('https://techwithtim.net/')

def clickElement(locator):
  # Retry finding/clicking element if it fails the first time
  retry_limit = 2
  for retry_count in range(retry_limit):
    try:
      element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locator))
      element.click()
      break
    except (ElementClickInterceptedException, TimeoutException) as e:
      if retry_count == retry_limit - 1:
        print(str(type(e).__name__) + str(locator))
        raise
    except Exception:
      print(traceback.format_exc())
      raise

# Navigate through Tim's website
try:
  clickElement((By.LINK_TEXT, 'Tutorials'))      
  clickElement((By.XPATH, '//h3[contains(text(), "Learn python programming.")]'))
  clickElement((By.XPATH, '//h3[text() = "Python for complete beginners."]'))
  clickElement((By.CSS_SELECTOR, 'a[class^="navigation__NavigationItem"]'))
  driver.back()
  driver.forward()
except:
  driver.quit()