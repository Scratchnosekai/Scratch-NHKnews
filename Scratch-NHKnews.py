import requests
import scratchattach as sa
from bs4 import BeautifulSoup
import time

url_4 = "http://www3.nhk.or.jp/rss/news/cat4.xml"
url_6 = "http://www3.nhk.or.jp/rss/news/cat6.xml"
r_4 = requests.get(url_4)
r_6 = requests.get(url_6)
xml_4=r_4.text
xml_6=r_6.text

year=datetime.year
month=datetime.month
day=datetime.day

xml_6 = find_all((year)(month)(day))	
print(xml_6)


