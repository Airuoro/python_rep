import requests
import re

f = open("哔哩热门.csv", mode="a+", encoding="utf-8")

num = range(2)
for i in num:
    params = {
        "ps": "20",
        "pn": str(num[i] + 1)
    }
    url = "https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1"
    resp = requests.get(url)
    # print(resp.json()['data'])
    data = resp.json()['data']['list']
    # print(data)
    for item in data:
        tname = item['tname']
        title = item['title']
        pub_location = item['pub_location']
        owner_name = item['owner']['name']
        print(tname, owner_name, title, pub_location)
        f.write(f"{tname}, {owner_name}, {title}, {pub_location}\n")
