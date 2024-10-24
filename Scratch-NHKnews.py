import requests
import scratchattach as sa
from bs4 import BeautifulSoup
import datetime

tokyo_tz = datetime.timezone(datetime.timedelta(hours=9))
dt = datetime.datetime.now(tokyo_tz)

url_4 = "http://www3.nhk.or.jp/rss/news/cat4.xml"
url_6 = "http://www3.nhk.or.jp/rss/news/cat6.xml"
r_4 = requests.get(url_4)
r_6 = requests.get(url_6)
xml_4=r_4.text
xml_6=r_6.text
r_4.find_all(dt.year)




