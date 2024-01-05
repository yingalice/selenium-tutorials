from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# Get date, views, title of each video
try:
  driver.get('https://www.twitch.tv/bbytesizedd/videos?filter=all&sort=time')
  wait = WebDriverWait(driver, 5)
  videos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-a-target^="video-tower-card"]')))
  for idx, video in enumerate(videos):
    image = video.find_element(By.CSS_SELECTOR, 'article>div:nth-child(2) a img.tw-image')
    release_date = image.get_attribute('title')
    views = video.find_element(By.CSS_SELECTOR, 'article a>div>div:nth-child(3)>div')
    title = video.find_element(By.CSS_SELECTOR, 'a>h3')
    print(str(idx) + ': ' + release_date + ' - ' + views.text + ' - ' + title.text)
finally:
  driver.quit()