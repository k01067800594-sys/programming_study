from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 크롬브라우저 실행
driver = webdriver.Chrome()
# 주소 접속
driver.get("https://danawa.com/?srsltid=AfmBOoqEs5vQQi6u3NSreNGRpzMqcbJVq7hAe_J0skaBwnzYbNfLLzxx")

# 상품명 접근
names = driver.find_elements(By.CLASS_NAME, 'goods_title')

for n in names:
    print(n.text)

time.sleep(5)