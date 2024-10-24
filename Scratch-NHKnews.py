import requests
import scratchattach as sa
from bs4 import BeautifulSoup
import datetime

url_4 = "http://www3.nhk.or.jp/rss/news/cat4.xml"
url_6 = "http://www3.nhk.or.jp/rss/news/cat6.xml"
r_4 = requests.get(url_4)
r_6 = requests.get(url_6)
xml_4=r_4.text
xml_6=r_6.text

date = datetime.datetime.now()
num1 = date.year
num2 = date.month
num3 = date.day
result = str(num1) + str(num2) + str(num3)

l = BeautifulSoup(r_4.text,'xml')
for item in l.find_all('item'):
        guid = item.find('guid').text.strip()
        if guid.isdigit() and int(guid) > result:  
            title = item.find('title').text.strip()
            link = item.find('link').text.strip()
            pubDate = item.find('pubDate').text.strip()
            print(f"タイトル: {title}")
            print(f"リンク: {link}")
            print(f"公開日時: {pubDate}")


