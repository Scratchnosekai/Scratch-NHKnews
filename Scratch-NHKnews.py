import requests
from bs4 import BeautifulSoup
import datetime

def fetch_and_parse_rss(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'xml')
    return soup

url = "http://www3.nhk.or.jp/rss/news/cat4.xml"

soup = fetch_and_parse_rss(url)

three_days_ago = datetime.datetime.now() - datetime.timedelta(days=3)

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
