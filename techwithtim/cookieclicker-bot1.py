from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import inspect

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://orteil.dashnet.org/cookieclicker/')

def isElementInvisible(locator):
  # Check if element is gone (ie. loading screen)
  try:
    return WebDriverWait(driver, 5).until(EC.invisibility_of_element((locator)))
  except TimeoutException as e:
    print(inspect.stack()[0][3] + ': ' + str(type(e).__name__) + str(locator))
    raise

def getClickableElement(locator, click = False):
  # Retry finding/clicking an element if it fails the first time
  retry_limit = 2
  for retry_count in range(retry_limit):
    try:
      element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((locator)))
      if click:
        element.click()
      return element
    except (StaleElementReferenceException, TimeoutException) as e:
      if retry_count == retry_limit - 1:
        print(inspect.stack()[0][3] + ': ' + str(type(e).__name__) + str(locator))
        raise

def playGame():
  # Continuously click on cookie to earn cookies
  # Whenever there's enough cookies, buy an upgrade (prefer the better item)
  try:
    cookie = getClickableElement((By.ID, 'bigCookie'))
    cookie_count = getClickableElement((By.ID, 'cookies'))
    items = [driver.find_element(By.ID, 'productPrice' + str(i)) for i in range (1, -1, -1)]
    actions = ActionChains(driver)
    upgrade_actions = ActionChains(driver)
    for i in range(100):
      actions.move_to_element(cookie).click().perform()
      count = int(cookie_count.text.split(" ")[0])
      for item in items:
        value = int(item.text)
        if value <= count:
          upgrade_actions.move_to_element(item).click().perform()
  except NoSuchElementException as e:
    print(inspect.stack()[0][3] + ': ' + str(type(e).__name__))
    raise

try:
  # Select English language and play the game 
  # In both cases, first wait for the loading screen to disappear
  if isElementInvisible((By.ID, 'loading')):
    lang = getClickableElement((By.ID, 'langSelect-EN'), True)
  if isElementInvisible((By.ID, 'loading')):
    playGame()
except:
  driver.quit()