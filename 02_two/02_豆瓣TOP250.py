# 思路
# 1. 拿到页面源代码
# 2. 编写正则，提取页面数据
# 3. 保存数据
import requests
import re

f = open("top250.csv", mode="w", encoding='utf-8')
url = "https://movie.douban.com/top250";
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
for i in range(25):
    params = {
        "start" : i * 25
    }
    resp = requests.get(url, headers=headers, params=params)
    pageSource = resp.text

    # 编写正则表达式
    # re.S 可以让正则中的.匹配换行符
    obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?导演: (?P<dao>.*?)&nbsp;.*?<br>'
                     r'(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">'
                     r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)

    # 进行正则匹配
    result = obj.finditer(pageSource)
    for item in result:
        name = item.group("name")
        dao = item.group("dao")
        year = item.group("year").strip() # 去掉字符串左右两侧的空白
        score = item.group("score")
        num = item.group("num")
        f.write(f"{name},{dao},{year},{score},{num}\n") # 如果感觉low，可以更换csv模块，写入数据

f.close()
resp.close()
print("豆瓣TOP250提起完毕")

# 如何翻页提取?
# (页数 - 1) * 25
