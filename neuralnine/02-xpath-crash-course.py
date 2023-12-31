from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

url = 'https://books.toscrape.com/'
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = Chrome(options=chrome_options)
driver.get(url)
driver.maximize_window()

# Get titles and prices of books with one star ratings
xpath_query = '//article[p[@class="star-rating One"]]//h3/a | //article[p[@class="star-rating One"]]//p[@class="price_color"]'
results = driver.find_elements('xpath', xpath_query)

for result in results:
  if result.tag_name == 'a':
    print(result.get_attribute('title'))
  elif result.tag_name == 'p':
    print(result.get_attribute('innerHTML'))

# Other Xpath queries covered in the video:
# //article//a/@title  **Note: Need to remove /@title and filter for title attribute in Python, since find_element(s) expects element
# //article//a/..
# //a[@title]
# //div[contains(@class, 'col-sm-8')]
# //*[text()[contains(., 'Book')]]
# //*[count(.//li)=20]/li
# //div/following-sibling::div
# //div[@id="promotions_left"]/following-sibling::div[1]
# //div[ancestor::article]