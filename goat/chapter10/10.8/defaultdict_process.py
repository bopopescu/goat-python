# coding: utf-8

from collections import defaultdict
s = [('Python', 1), ('Swift', 2), ('Python', 3), ('Swift', 4), ('Python', 9)]
# 创建defaultdict，设置由list()函数来生成默认值
d = defaultdict(list)
for k, v in s:
    # 直接访问defaultdict中指定key对应的value即可。
    # 如果该key不存在，defaultdict会自动为该key生成默认值
    d[k].append(v)
print(list(d.items()))
