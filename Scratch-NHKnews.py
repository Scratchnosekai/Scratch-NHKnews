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

timezone = pytz.timezone('Asia/Tokyo')

# 3日前の日時を取得し、タイムゾーン情報を追加
three_days_ago = datetime.datetime.now(timezone) - datetime.timedelta(days=3)

# ニュースアイテムをループで処理
for item in soup.find_all('item'):
        if pubDate >= three_days_ago:
            title = item.find('title').text.strip()
            link = item.find('link').text.strip()
            print(f"タイトル: {title}")
            print(f"リンク: {link}")
            print(f"公開日時: {pubDate}")
            print("-" * 20)
    except ValueError:
        print(f"日付の解析に失敗しました: {pubDate_str}")
