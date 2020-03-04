# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 12:34
# @Author  : 64274
# @Desc    : 
# @File    : __init__.py.py
# @Software: PyCharm

import urllib.request as re

def load_data():
    # url = "https://www.baidu.com"
    url = "https://www.baidu.com"
    result = re.urlopen(url)
    print(result)

    # 读取内容 byte类型
    data = result.read();
    print(data)

    str_data = data.decode("utf-8")
    print(str_data)

load_data()

