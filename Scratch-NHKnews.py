import requests
from bs4 import BeautifulSoup
import datetime
import pytz
import scratchattach as sa
import os

session = sa.login("Scratchnosekai_2", os.getenv("PASSWORD"))
cloud = session.connect_cloud("876250500")

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
            continue

    return news_items

def convert_to_unicode_string(text):
    unicode_numbers = []
    for char in text:
        unicode_point = ord(char)
        unicode_numbers.append(f"{unicode_point:05d}")
    return ''.join(unicode_numbers)

urls = {
    "政治": "http://www3.nhk.or.jp/rss/news/cat4.xml",
    "国際": "http://www3.nhk.or.jp/rss/news/cat6.xml",
    "社会": "http://www3.nhk.or.jp/rss/news/cat1.xml",
    "スポーツ": "http://www3.nhk.or.jp/rss/news/cat7.xml",
    "文化・エンタメ": "http://www3.nhk.or.jp/rss/news/cat2.xml",
    "科学・医療": "http://www3.nhk.or.jp/rss/news/cat3.xml"
}

cloud_vars = {f"From_Host{i}": "" for i in range(1, 10)}
news_count = 0

for category, url in urls.items():
    news_list = fetch_and_parse_rss(url, category)

    if news_list:
        for news in news_list:
            if news_count < len(cloud_vars):
                text = news['title']
                unicode_numbers = convert_to_unicode_string(text)
                pubDate = news['pubDate'].strftime('%Y-%m-%d %H:%M:%S')
                
                cloud_vars[f"From_Host{news_count + 1}"] = unicode_numbers
                
                print(f"【{category}】")
                print(f"タイトル: {news['title']}")
                print(f"リンク: {news['link']}")
                print(f"公開日時: {pubDate}")
                print(f"Unicode数値: {unicode_numbers}")
                
                news_count += 1
            else:
                break
    else:
        print(f"{category}カテゴリには新しいニュースがありません。")

cloud.set_vars(cloud_vars)
