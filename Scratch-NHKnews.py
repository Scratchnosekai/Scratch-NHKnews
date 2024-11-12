import requests
from bs4 import BeautifulSoup
import datetime
import pytz
import os

def fetch_and_parse_rss(url, category):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'xml')
    news_items = []
    
    for item in soup.find_all('item'):
        pubDate_str = item.find('pubDate').text.strip()
        try:
            pubDate = datetime.datetime.strptime(pubDate_str, '%a, %d %b %Y %H:%M:%S %z')
            if pubDate >= datetime.datetime.now(pytz.timezone('Asia/Tokyo')) - datetime.timedelta(days=3):
                news_items.append({
                    'category': category,
                    'title': item.find('title').text.strip(),
                    'link': item.find('link').text.strip(),
                    'pubDate': pubDate
                })
        except ValueError:
            print(f"日付の解析に失敗しました: {pubDate_str}")
            continue  
    
    return news_items  

urls = {
    "政治": "http://www3.nhk.or.jp/rss/news/cat4.xml",
    "国際": "http://www3.nhk.or.jp/rss/news/cat6.xml",
    "社会": "http://www3.nhk.or.jp/rss/news/cat1.xml",
    "スポーツ": "http://www3.nhk.or.jp/rss/news/cat7.xml",
    "文化・エンタメ": "http://www3.nhk.or.jp/rss/news/cat2.xml",  
    "科学・医療": "http://www3.nhk.or.jp/rss/news/cat3.xml"
}


for category, url in urls.items():
    news_items = fetch_and_parse_rss(url, category)
    
    if news_items:  
        for item in news_items:
            else:
    print(f"{category}カテゴリには最新のニュースがありません。")
