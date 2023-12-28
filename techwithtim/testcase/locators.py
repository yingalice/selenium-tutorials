from selenium.webdriver.common.by import By

# Best practice to separate locators from where they're being used
# Locators of the same page belong to the same class

class MainPageLocators(object):
  # Class for main page locators
  GO_BUTTON = (By.ID, 'submit')

class SearchResultsPageLocators(object):
  # Class for search results locators
  pass