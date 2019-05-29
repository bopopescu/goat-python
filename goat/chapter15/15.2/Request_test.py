# coding: utf-8

from urllib.request import *

params = 'put请求数据'.encode('utf-8')
# 创建Request对象，设置使用PUT请求
req = Request(url='http://localhost:8888/test/put',
    data=params, method='PUT')
with urlopen(req) as f:
    print(f.status)
    print(f.read().decode('utf-8'))

# 创建Request对象
req = Request('http://localhost:8888/test/header.jsp')
# 添加请求头
req.add_header('Referer', 'http://www.crazyit.org/')
with urlopen(req) as f:
    print(f.status)
    print(f.read().decode('utf-8'))
