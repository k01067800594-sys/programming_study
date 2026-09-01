from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def scroll_fun():
    while True:
    #스크롤 하기 전  높이
        h1 = driver.execute_script(
            "return document.documentElement.scrollHeight")
    # print("첫번째 높이", h1)
    # 스크롤을 현재높이 만큼 내리기
        driver.execute_script(
            "window.scrollTo(0,document.documentElement.scrollHeight)")
    # 영상 로딩 시간(잠시 대기)
        time.sleep(2)
    #스크롤 내린 뒤 높이 값
        h2= driver.execute_script(
            "return document.documentElement.scrollHeight")
        # print("두번 째 높이:", h2)
    # 스크롤 전, 후 높이 비교
        if h1 == h2  :
            break

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=%EC%9D%B8%EA%B8%B0%EA%B8%89%EC%83%81%EC%8A%B9")
time.sleep(2)

search_input = driver.find_element(By.NAME, "search_query")
search_input.clear()
search_input.send_keys("승상싱")
search_input.send_keys(Keys.ENTER)

titles=driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')

scroll_fun()
titles=driver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')

title_list=[]
for t in titles:
    title_list.append(t.text)
print(f"총 {len(title_list)}개의 제목을 수집하였습니다")

c_result={
    "title":title_list
}
result = pd.DataFrame(c_result)

result.to_csv("./youtube_result.csv", encoding="utf-8-sig")