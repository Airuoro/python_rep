# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import requests
import re

url = "https://jn.zu.anjuke.com/"
params = {
    "t": "1",
    "from": "0",
    "comm_exist": "on",
    "kw": "草山岭",
}
resp = requests.get(url, params=params)
obj = re.compile(r'<a data-company="" class="img".*?href="(?P<url>.*?)".*?<img alt="(?P<name>.*?)'
                 r'".*?<p><strong><b class="strongbox">(?P<price>.*?)</b>', re.S)
pageSource = resp.text
result = obj.finditer(pageSource)
print(result)
for item in result:
    url = item.group("url")
    name = item.group("name")
    price = item.group("price")
    print(name, price, url)
