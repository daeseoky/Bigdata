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

while True:

    print('count :', count)

    # 기상청 날씨누리
    browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')


    # 지역명 수집 후 지점 클릭
    tags_a_region = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr > td:nth-child(1) > a')
    region = tags_a_region[count - 1].text
    tags_a_region[count - 1].click()
    logger.info(f'지역명 : {region}')
    print('지역 :', region)

    # 파일 디렉토리 생성
    dir = "./weather/{:%Y-%m-%d}".format(datetime.now())

    if not os.path.exists(dir):
        os.makedirs(dir)

    # 파일 생성 및 데이터 파싱
    fname = "{:%Y-%m-%d-%H-%M.csv}".format(datetime.now())
    file = open(dir + '/' + fname, 'w', encoding='utf-8')


    # 시간별 날씨 세부사항 출력
    step = 1
    while True:
        tag_lis = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')
        for li in tag_lis:
            td = li.find_element(By.CSS_SELECTOR, '#weather_table > tbody > tr > td').text


            # reple = li.find_element(By.CSS_SELECTOR, '.score_reple > p > span:last-child').text

            #print('{},{},{}'.format(step, region, td))
            # logger.info('{},{}'.format(count, title))
            # file.write('{},{},{},{}\n'.format(count, title, reple, score))

            step += 1


        if step > 48:
            break

    count += 1




    # for tag in tags_a_region:
    #     print(tag.text)
