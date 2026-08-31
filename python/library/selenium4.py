from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 크롬브라우저 실행
driver = webdriver.Chrome()
# 주소 접속
driver.get("https://danawa.com/?srsltid=AfmBOoqEs5vQQi6u3NSreNGRpzMqcbJVq7hAe_J0skaBwnzYbNfLLzxx")

s_element = driver.find_element(By.XPATH, '//*[@id="AKCSearch"]')

s_element.send_keys("마우스")
# s_element.send_keys(Keys.ENTER)
btn=driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/div/button')
btn.click()

time.sleep(10)