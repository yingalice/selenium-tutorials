import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
  # Sample test case to demonstrate page objects
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.get('https://www.python.org')

  def test_search_python(self):
    # On python.org, search for 'pycon', and verify that results show up (ie. not empty)
    main_page = page.MainPage(self.driver)
    self.assertTrue(main_page.is_title_matches(), "Python.org title doesn't match")
    main_page.search_text_element = 'pycon'
    main_page.click_go_button()
    search_result_page = page.SearchResultPage(self.driver)
    self.assertTrue(search_result_page.is_results_found(), 'No results found')

  def tearDown(self):
    self.driver.close()

# Only executes if we run this module directly, and not if it's being imported
if __name__ == '__main__':
  unittest.main()