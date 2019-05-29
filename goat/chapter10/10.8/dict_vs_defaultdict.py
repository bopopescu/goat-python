# coding: utf-8

from collections import defaultdict
my_dict = {}
# 使用int作为defaultdict的default_factory
# 将key不存在时，将会返回int()函数的返回值
my_defaultdict = defaultdict(int)
print(my_defaultdict['a']) # 0
print(my_dict['a']) # KeyError