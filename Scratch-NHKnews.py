import requests
import scratchattach as sa

url="http://www3.nhk.or.jp/rss/news/cat4.xml"
a=requests.get(url)
a.text
