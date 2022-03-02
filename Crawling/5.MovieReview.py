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

# 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

rank = 1
page = 1

while True:
    # 네이버 영화 랭크
    browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&page=%d' % page)

    # 영화 제목 클릭

    tags_a_titles = browser.find_elements(By.CSS_SELECTOR, '#old_content > table > tbody > tr > td.title > div > a')
    tags_a_titles[rank -1].click()
    # for tag in tags_a_titles:
    #     print(tag.text)

    # 영화 평점 클릭
    tags_a_tab5 = browser.find_element(By.CSS_SELECTOR, '#movieEndTabMenu > li:nth-child(5) > a')
    tags_a_tab5.click()

    # 영화 제목 수집
    title = browser.find_element(By.CSS_SELECTOR, '#content > div.article > div.mv_info_area > div.mv_info > h3 > a').text
    
    # 현재 가상 브라우저의 제어를 영화리뷰 iframe으로 전환
    browser.switch_to.frame('pointAfterListIframe')

    # 파일 디렉토리 생성
    dir = "./weather/{:%Y-%m-%d}".format(datetime.now())

    if not os.path.exists(dir):
        os.makedirs(dir)

    # 파일 생성 및 데이터 파싱
    fname = "{:%Y-%m-%d-%H-%M.csv}".format(datetime.now())
    file = open(dir + '/' + fname, 'w', encoding='utf-8')

    # 영화 리뷰 출력
    count = 1
    while True:
        tag_lis = browser.find_elements(By.CSS_SELECTOR, 'body > div > div > div.score_result > ul > li')
        for li in tag_lis:
            score = li.find_element(By.CSS_SELECTOR, '.star_score > em').text
            reple = li.find_element(By.CSS_SELECTOR, '.score_reple > p > span:last-child').text

            print('{},{},{},{}'.format(count, title, reple, score))
            file.write('{},{},{},{}'.format(count, title, reple, score))

            count += 1

        # 다음 페이지 버튼 클릭
        try:
            tag_a_next = browser.find_element(By.CSS_SELECTOR, 'body > div > div > div.paging > div > a.pg_next')
            tag_a_next.click()
        except:
            break

    # 다음 순위 영화
    rank += 1

    if rank > page * 50:
        # 랭킹 페이지 다음버튼 클릭
        page += 1

        if page > 40:
            #최종 종료
            break

print('종료...')





