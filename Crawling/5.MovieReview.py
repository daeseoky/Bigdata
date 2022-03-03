"""
날짜 : 2022/03/02
이름 : 양대석
내용 : 파이썬 영화 리뷰 크롤링 실습
"""
import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import logging
import time

# 로거 생성
logger = logging.getLogger('movie_logger')
logger.setLevel(logging.INFO)

# 포거 포멧설정
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 로그 핸들러
log_handler = logging.FileHandler('./movie_review.log')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)


# 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')
logger.info('가상브라우저 실행...')


rank = 1
page = 1

while True:
    # 네이버 영화 랭크
    browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&page=%d' % page)
    logger.info('네이버 영화 랭킹 {}페이지이동...'.format(page))

    # 영화 제목 클릭
    tags_a_titles = browser.find_elements(By.CSS_SELECTOR, '#old_content > table > tbody > tr > td.title > div > a')
    # logger.info('{}. {}영화 제목 클릭...'.format(rank, tags_a_titles[rank - 1].text))
    tags_a_titles[rank-1].click()

    # for tag in tags_a_titles:
    #     print(tag.text)

    # 영화 평점 클릭
    tags_a_tab5 = browser.find_element(By.CSS_SELECTOR, '#movieEndTabMenu > li > a[title="평점"]')
    tags_a_tab5.click()
    logger.info('영화 평점 클릭...')

    # 영화 제목 수집
    title = browser.find_element(By.CSS_SELECTOR, '#content > div.article > div.mv_info_area > div.mv_info > h3 > a').text
    logger.info(f'영화 제목 수집 : {title}')

    # 현재 가상 브라우저의 제어를 영화리뷰 iframe으로 전환
    browser.switch_to.frame('pointAfterListIframe')
    logger.info('iframe으로 전환')

    # 파일 디렉토리 생성
    dir = "./weather/{:%Y-%m-%d}".format(datetime.now())

    if not os.path.exists(dir):
        os.makedirs(dir)

    # 파일 생성 및 데이터 파싱
    fname = "{:%Y-%m-%d-%H.csv}".format(datetime.now())
    file = open(dir + '/' + fname, 'w', encoding='utf-8')

    # 영화 리뷰 출력
    count = 1
    while True:
        tag_lis = browser.find_elements(By.CSS_SELECTOR, 'body > div > div > div.score_result > ul > li')
        for li in tag_lis:
            score = li.find_element(By.CSS_SELECTOR, '.star_score > em').text
            reple = li.find_element(By.CSS_SELECTOR, '.score_reple > p > span:last-child').text

            print('{},{},{},{}'.format(count, title, reple, score))
            logger.info('{},{}'.format(count, title))
            file.write('{},{},{},{}\n'.format(count, title, reple, score))

            count += 1

        # 다음 페이지 버튼 클릭
        try:
            tag_a_next = browser.find_element(By.CSS_SELECTOR, 'body > div > div > div.paging > div > a.pg_next')
            tag_a_next.click()
            logger.info('다음페이지 클릭')
        except:
            logger.error('{} 수집완료'.format(title))
            break

    # 다음 순위 영화
    rank += 1

    if rank > 50:
        # 랭킹 페이지 다음버튼 클릭
        page += 1
        rank = 1

        if page > 40:
            # 최종 종료
            break

logger.info('크롤링 종료...')





