import requests
import json

url = "https://fanyi.baidu.com/sug"

data = {
    "kw" : input("请输入一个单词")
}

resp = requests.post(url, data = data)

print(resp.text) # 此时拿到的是文本字符串
print(resp.json()['data']) # 此时拿到的是json数据
