"""
날짜 : 2022/02/28
이름 : 양대석
내용 : 파이썬 파싱 요청 실습

     크롤링
        - 웹페이지 데이터 수집하는 기술
        - 크롤러(봇)을 정해진 규칙에 따라 페이지를 이동하면서 데이터를 수집하는 기술

     파싱(Parsing)
        - 문서 해독
        - 마크업 문서(HTML, XML)에서 특정 태그의 데이터를 추출 가공 처리하는 과정
"""
import requests as req
from bs4 import BeautifulSoup as bs

# # 페이지 요청
# html = req.get('http://chhak.or.kr/test.html').text
# print(html)
#
# # 문서객체 생성
# dom = bs(html, 'html.parser')
# print(dom)
#
# # 데이터 파싱
# title = dom.html.body.h3.text
# print('title : ',title)
#
# rs1 = dom.select_one('#seoul').text
# rs2 = dom.select_one('.busan').text
# print('rs1 : ', rs1)
# print('rs2 : ', rs2)
#
# lis = dom.select('ul > li')
#
# for li in lis:
#     print('li text : ', li.text)
#
# print('-'*30)

# 네이버 IT뉴스 파싱하기
# 페이지 요청
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'

# 크롤링 방지를 위한 보안을 통과하기 위해 유저 지정을 브라우져로 해줌
result = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text


# 문서객체 생성
dom = bs(result, 'html.parser')

# 파싱하기
tags = dom.select('#main_content > div.list_body.newsflash_body > ul > li > dl > dt:not(.photo) > a')

for i in tags:
    print('a text : ', i.text.strip())
