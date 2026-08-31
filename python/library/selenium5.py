from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://comic.naver.com/webtoon?tab=mon")

time.sleep(5)

web_class=driver.find_elements(By.CLASS_NAME, 'text')


for c in web_class:
    print(c.text)
print(len(web_class))