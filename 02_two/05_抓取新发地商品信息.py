import time

import requests
import re
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/getPriceData.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
num = range(2)
for i in num:
    data = {
        "limit": "20",
        "current": num[i] + 1
    }
    resp = requests.post(url, data=data)
    # print(resp.json()['list'])

    vegetable_list = resp.json()['list']
    for vegetable in vegetable_list:
        prodName = vegetable['prodName'] # 菜名
        lowPrice = vegetable['lowPrice'] # 最低价
        avgPrice = vegetable['avgPrice'] # 平均价
        highPrice = vegetable['highPrice'] # 最高价
        specInfo = vegetable['specInfo'] # 规格
        place = vegetable['place'] # 产地
        unitInfo = vegetable['unitInfo'] # 单位
        pubDate = vegetable['pubDate'] # 单位
        print(prodName, lowPrice, avgPrice, highPrice, specInfo, place, unitInfo, pubDate)
        with open("新发地菜价.csv", mode="a+", encoding="utf-8") as f:
            f.write(f"{prodName}, {lowPrice}, {avgPrice}, {highPrice}, {specInfo}, {place}, {unitInfo}, {pubDate}\n")
f.close()
resp.close()
print("新发地菜价抓取成功！")