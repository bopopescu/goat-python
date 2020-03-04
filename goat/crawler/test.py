# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 12:37
# @Author  : 64274
# @Desc    : 
# @File    : test.py
# @Software: PyCharm

#导入requests库
import requests
url = 'http://www.cntour.cn/'
#Get方式获取网页数据
strhtml = requests.get(url)

print(strhtml.text)