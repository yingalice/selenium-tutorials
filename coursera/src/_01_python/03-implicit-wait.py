from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# The page_load_strategy option was only added to show the 
# NoSuchElementException error that occurred before we added the implicit wait
# (makes find_element return immediately).  
# Usually do not get the error, since Twitch loads so fast
options = Options()
options.page_load_strategy = 'none'
driver = webdriver.Chrome(options = options)
driver.get('https://www.twitch.tv/bbytesizedd/videos')

# Implicit wait applies to find_element(s)
driver.implicitly_wait(2)
cookies = driver.find_element(By.CSS_SELECTOR, 'img.tw-image')
print(cookies.tag_name)

driver.quit()