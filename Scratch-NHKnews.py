import requests
from bs4 import BeautifulSoup
import datetime
import pytz
import scratchattach as sa
from scratchattach import Encoding
import os

r=requests.get("https://www3.nhk.or.jp/nhkworld/en/news/")
a=r.text
print(a)
