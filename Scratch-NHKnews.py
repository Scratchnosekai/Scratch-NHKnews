import requests
import scratchattach as sa

url_politics="http://www3.nhk.or.jp/rss/news/cat4.xml"
url_international="http://www3.nhk.or.jp/rss/news/cat6.xml"
r=requests.get(url_politics)(url_international)
xml=r.text
print(xml)

