import requests
from bs4 import BeautifulSoup
import datetime
import pytz

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
    """ 文字列をUnicodeのコードポイントに変換して4桁形式で返す """
    unicode_numbers = ""
    for char in text:
        unicode_point = ord(char)  
        unicode_numbers += f"{unicode_point:04d}"  
    return unicode_numbers

urls = {
    "政治": "http://www3.nhk.or.jp/rss/news/cat4.xml",
    "国際": "http://www3.nhk.or.jp/rss/news/cat6.xml",
    "社会": "http://www3.nhk.or.jp/rss/news/cat1.xml",
    "スポーツ": "http://www3.nhk.or.jp/rss/news/cat7.xml",
    "文化・エンタメ": "http://www3.nhk.or.jp/rss/news/cat2.xml",
    "科学・医療": "http://www3.nhk.or.jp/rss/news/cat3.xml"
}

for category, url in urls.items():
    news_list = fetch_and_parse_rss(url, category)

    if news_list:
        for news in news_list:
            text = news['title']
            unicode_numbers = convert_to_unicode_string(text)  
            pubDate = news['pubDate'].strftime('%Y-%m-%d %H:%M:%S')  
            print(f"【{category}】")
            print(f"タイトル: {news['title']}")
            print(f"リンク: {news['link']}")
            print(f"公開日時: {pubDate}")
            print(f"Unicode数値: {unicode_numbers}")
    else:
        print(f"{category}カテゴリには新しいニュースがありません。")
