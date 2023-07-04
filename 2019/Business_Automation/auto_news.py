# 기사를 가져와서 엑셀로 만들기

# RSS 분석을 위해 필요한 라이브러리
import feedparser
from urllib.parse import quote
######################

# 엑셀파일을 생성하기 위한 라이브러리
from openpyxl import Workbook
#############################
import ssl

keywords = ["데이터","경제","과학기술","건강"]
base_rss_url_pre = 'https://news.google.com/rss/search?q='
base_rss_url_end = '&hl=ko&gl=KR&ceid=KR:ko'

urls = []

for keyword in keywords:
    urls.append(base_rss_url_pre + quote(keyword) + base_rss_url_end)


xlsx = Workbook()

ssl._create_default_https_context = ssl._create_unverified_context

for i in range(len(keywords)):
    sheet = xlsx.create_sheet(keywords[i])
    sheet.append(["기사 제목", "링크", "날짜"])
    
    news_list = feedparser.parse(urls[i])

    for news in news_list['items']:
        sheet.append([news['title'], news['link'], news['published']])

file_name = "name_list.xlsx"
xlsx.save(file_name)
print("저장 완료!!!")







