import requests
from bs4 import BeautifulSoup
import datetime
import pytz

def fetch_and_parse_rss(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'xml')
    return soup

url = "http://www3.nhk.or.jp/rss/news/cat4.xml"

timezone = pytz.timezone('Asia/Tokyo')

three_days_ago = datetime.datetime.now(timezone) - datetime.timedelta(days=3)

for item in soup.find_all('item'):
    pubDate_str = item.find('pubDate').text.strip()
    try:
        pubDate = datetime.datetime.strptime(pubDate_str, '%a, %d %b %Y %H:%M:%S %z')
        if pubDate >= three_days_ago:
            title = item.find('title').text.strip()
            link = item.find('link').text.strip()
            print(f"タイトル: {title}")
            print(f"リンク: {link}")
            print(f"公開日時: {pubDate}")
            print("-" * 20)
    # The indentation of the except block should be at the same level as the try block
    except ValueError:
        print(f"日付の解析に失敗しました: {pubDate_str}")
