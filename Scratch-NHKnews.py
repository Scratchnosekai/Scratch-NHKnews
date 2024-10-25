import requests
from bs4 import BeautifulSoup
import datetime
import pytz
import scratchattach as sa
from scratchattach import Encoding
import os

def fetch_and_parse_rss(url, category):
    """Fetches and parses the RSS feed from the given URL and category.

    Args:
        url: The URL of the RSS feed.
        category: The category of news (e.g., "政治", "国際", "社会").

    Returns:
        A list of news items.
    """

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

    return news_items

session = sa.login("Scratchnosekai", os.getenv("PASSWORD"))
cloud = session.connect_cloud("876250500")
encode= Encoding.encode("aiueo")
print(encode)
print(decode)
urls = {
    "政治": "http://www3.nhk.or.jp/rss/news/cat4.xml",
    "国際": "http://www3.nhk.or.jp/rss/news/cat6.xml",
    "社会": "http://www3.nhk.or.jp/rss/news/cat1.xml"
}

for category, url in urls.items():
    news_items = fetch_and_parse_rss(url, category)

    for item in news_items:
        print(f"{item['category']}")
        print(f"タイトル: {item['title']}")
        print(f"リンク: {item['link']}")
        print(f"公開日時: {item['pubDate']}")
        print("-" * 20)
        

