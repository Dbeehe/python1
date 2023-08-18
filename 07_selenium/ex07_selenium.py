from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://comic.naver.com/webtoon")
time.sleep(3)
# 웹툰 접근
titles = driver.find_elements(By.CLASS_NAME, 'text')

for title in titles:
    print(title.text)
print(len(titles))
