import requests
from bs4 import BeautifulSoup
import datetime
import pytz
import scratchattach as sa
import os

def fetch_and_parse_rss(url, category):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'xml')
    news_items = []
    
    # RSSフィードの項目をループ
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
            continue  # 日付解析に失敗した場合は次のアイテムに進む
    
    return news_items  # 必ずnews_itemsを返す

# ログインしてクラウド接続
session = sa.login("Scratchnosekai", os.getenv("PASSWORD"))
cloud = session.connect_cloud("876250500")

# URL 辞書の修正: カンマを追加
urls = {
    "政治": "http://www3.nhk.or.jp/rss/news/cat4.xml",
    "国際": "http://www3.nhk.or.jp/rss/news/cat6.xml",
    "社会": "http://www3.nhk.or.jp/rss/news/cat1.xml",
    "スポーツ": "http://www3.nhk.or.jp/rss/news/cat7.xml",
    "文化・エンタメ": "http://www3.nhk.or.jp/rss/news/cat2.xml",  # カンマ追加
    "科学・医療": "http://www3.nhk.or.jp/rss/news/cat3.xml"
}

# 各カテゴリに対するニュースを処理
for category, url in urls.items():
    news_items = fetch_and_parse_rss(url, category)
    
    if news_items:  # news_itemsが空でない場合に処理
        for item in news_items:
            print(f"{item['category']}")
            print(f"タイトル: {item['title']}")
            print(f"リンク: {item['link']}")
            print(f"公開日時: {item['pubDate']}")
            print("-" * 20)
    else:
        print(f"{category}カテゴリには最新のニュースがありません。")
