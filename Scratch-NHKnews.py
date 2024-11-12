import requests
from bs4 import BeautifulSoup
import datetime
import pytz
import os

# ... (これまでのコードは省略)

for category, url in urls.items():
    news_items = fetch_and_parse_rss(url, category)

    if news_items:
        for item in news_items:
            text = "こんにちは、Scratchnosekai!！"
            result = ""
            for char in text:
                result += str(ord(char))
            print(f"{category}カテゴリの最新ニュース: {item['title']}\n"
                  f"リンク: {item['link']}\n"
                  f"Unicode数値: {result}")
    else:
        print(f"{category}カテゴリには最新のニュースがありません。")
