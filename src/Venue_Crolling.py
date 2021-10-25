import requests
from bs4 import BeautifulSoup
import pandas as pd

file = open("C:/Users/yuno/Desktop/데이터시각화/그거/잉글랜드.txt", 'r')
lines = file.readlines()
con_name = []
value_name = []

for line in lines:
    con_name.append(line[:-1])

del con_name[0]


def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html

for i in range(0, len(north_island)):
    URL = "https://ko.foursquare.com/v/" + con_name[i]
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(id="h1")
    venues = soup.find_all(class_="venueName")
    name = venues[0].text.replace('\n', '').replace('\t', '').replace(' ', '')
    value_name.append(name)