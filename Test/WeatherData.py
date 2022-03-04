import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from datetime import datetime

# 로거 생성
logger = logging.getLogger('weather_logger')
logger.setLevel(logging.INFO)

# 포거 포멧설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 로그 핸들러
log_handler = logging.FileHandler('./weather_review.log')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)

# 가상 브라우저 실행
browser = webdriver.Chrome('../Crawling/chromedriver.exe')
logger.info('가상브라우저 실행...')
count = 1

# 기상청 날씨누리
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 파일 디렉토리 생성
dir = "./weather/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(dir):
    os.makedirs(dir)

# 파일 생성 및 데이터 파싱
fname = "{:%Y-%m-%d-%H-%M.csv}".format(datetime.now())
file = open(dir + '/' + fname, 'w', encoding='utf-8')

# 날씨 출력
tag_lis = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')
for li in tag_lis:
    td1 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text
    td2 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
    td4 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
    td5 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text
    td6 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text
    td7 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(7)').text
    td3 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
    td8 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(8)').text
    td9 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(9)').text
    td10 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(10)').text
    td11 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(11)').text
    td12 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(12)').text
    td13 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(13)').text
    td14 = li.find_element(By.CSS_SELECTOR, 'td:nth-child(14)').text

    file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(td1,td2,td3,td4,td5,td6,td7,td8,td9,td10,td11,td12,td13,td14))
logger.info('프로그램 완료')


