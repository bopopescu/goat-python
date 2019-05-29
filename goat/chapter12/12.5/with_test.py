# coding: utf-8

import codecs
# 使用with语句打开文件，该语句会负责关闭文件
with codecs.open("readlines_test.py", 'r', 'utf-8', buffering=True) as f:
    for line in f:
        print(line, end='')
