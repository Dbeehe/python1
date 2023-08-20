from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://www.youtube.com/")
time.sleep(3)
# 검색할 요소 접근

def scroll_fun():
    while True:
        # 스크롤 하기 전 높이
        before_scroll = driver.execute_script("return document.documentElement.scrollHeight")
        # 스크롤을 현재 높이 만큼 내리기
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        # 영상 로딩 시간
        time.sleep(2)
        # 스크롤 내린 후 높이 값
        after_scroll = driver.execute_script("return document.documentElement.scrollHeight")

        if before_scroll==after_scroll:
            break