import requests
from bs4 import BeautifulSoup
import datetime
import pytz
import scratchattach as sa
from scratchattach import Encoding
import os

session = sa.login("Scratchnosekai",os.getenv("PASSWORD")) 
cloud = session.connect_cloud("876250500") 
url = "http://www3.nhk.or.jp/rss/news/cat4.xml"
url2 = "http://www3.nhk.or.jp/rss/news/cat6.xml"

def fetch_and_parse_rss(url):
    """Fetches and parses the RSS feed from the given URL.

    Args:
        url: The URL of the RSS feed.

    Returns:
        A BeautifulSoup object representing the parsed RSS feed.
    """

    response = requests.get(url)
    response2 = requests.get(url2)
    response.raise_for_status()  
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'xml')  
    soup = BeautifulSoup(response2.content, 'xml')  
    return soup

soup = fetch_and_parse_rss(url)

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
    except ValueError:
        print(f"日付の解析に失敗しました: {pubDate_str}")

