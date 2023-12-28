from element import BasePageElement
from locators import MainPageLocators

# Page object pattern intends to create an object for each part of a webpage
# to build separation between test code and the code that interacts with webpage

class SearchTextElement(BasePageElement):
  # Locator for search box
  locator = 'q'

class BasePage(object):
  # Base class to initialize base page that will be called from all pages
  def __init__(self, driver):
    self.driver = driver

class MainPage(BasePage):
  # Home page action methods come here
  search_text_element = SearchTextElement()

  def is_title_matches(self):
    # Verifies 'Python' appears in page title
    return "Python" in self.driver.title
  
  def click_go_button(self):
    # Triggers the search
    element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
    element.click()

class SearchResultPage(BasePage):
  # Search results page action methods come here
  def is_results_found(self):
    # Search for text in page source (note: probably better to search on specific page element)
    return 'No results found.' not in self.driver.page_source