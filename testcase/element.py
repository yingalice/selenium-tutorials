from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BasePageElement(object):
  # Base page class that is initialized on every page object class
  def __set__(self, obj, value):
    # Sets text to value supplied
    driver = obj.driver
    WebDriverWait(driver, 100).until(
      lambda driver: driver.find_element(By.NAME, self.locator))
    driver.find_element(By.NAME, self.locator).clear()
    driver.find_element(By.NAME, self.locator).send_keys(value)

  def __get__(self, obj, owner):
    # Gets text of specified object
    driver = obj.driver
    WebDriverWait(driver, 100).until(
      lambda driver: driver.find_element(By.NAME, self.locator))
    element = driver.find_element(By.NAME, self.locator)
    return element.get_attribute('value')