"""
1.提取到主页面中的每一个电影的背后的那个url地址
    1.拿到 "2021必看热片"那一块的HTML代码
    2.从刚才拿到的HTML代码中提取到href的值
2.访问子页面，提取到电影的名称以及下载地址
"""
import time

import requests
import re

f = open("movieTop.csv", mode="w", encoding='utf-8')
url1 = "https://www.dy2018.com"
for i in range(2):
    if i == 0:
        url = "https://www.dy2018.com/html/tv/oumeitv/index.html"
    else:
        url = "https://www.dy2018.com/html/tv/oumeitv/index_" + str(i + 1) + ".html"
    resp = requests.get(url)
    resp.encoding = "gbk"
    pageSource = resp.text

    # print(resp.text)
    obj = re.compile(r'<td height="26">.*?<a href="(?P<download>.*?)"'
                     r' class="ulink" title="\d{4}年(美国|英国)电视剧(?P<name>.*?)》', re.S)
    result = obj.finditer(pageSource)
    for item in result:
        download = url1 + item.group("download")
        name = item.group("name") + "》"
        print(name, download)
        f.write(f"{name},{download}\n") # 如果感觉low，可以更换csv模块，写入数据
        time.sleep(1)
f.close()
resp.close()
print("电影天堂抓取成功！")






