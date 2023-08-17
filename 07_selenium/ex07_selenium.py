from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 접속할 주소
driver.get("https://comic.naver.com/webtoon")

# 웹툰 접근
webtoon_names = driver.find_elements(By.CSS_SELECTOR, '[name="productName"]')

for name in webtoon_names:
    print(webtoon_names)

time.sleep(10)