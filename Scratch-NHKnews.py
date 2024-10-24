import requests
import scratchattach as sa

url="http://www3.nhk.or.jp/rss/news/cat4.xml"
r=requests.get(url)
xml=r.text
print(xml)

