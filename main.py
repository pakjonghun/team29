import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.spartaWeb

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.naver.com/',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


lis = soup.select('#themecast > div.theme_cont > div:nth-child(1) > div > ul > li')
for li in lis:
    theme_category = li.select_one('a.theme_info > em').text
    content = li.select_one('a.theme_info > p').text
    a_tag = li.select_one('a.theme_info > strong').text
    source = li.select_one('a.theme_info > div > span.source > span').text
    date = li.select_one('a.theme_info > div > span.date').text
    # print(theme_category, content, a_tag, source, date)
    doc = {
        'theme_category':theme_category,
        'content':content,
        'a_tag':a_tag,
        'source':source,
        'date':date
    }
    db.news.insert_one(doc)