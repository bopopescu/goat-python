# coding: utf-8

from collections import OrderedDict
d = OrderedDict.fromkeys('abcde')
# 将b对应的key-value对移动到最右边（最后加入）
d.move_to_end('b')
print(d.keys()) # odict_keys(['a', 'c', 'd', 'e', 'b'])
# 将b对应的key-value对移动到最左边（最先加入）
d.move_to_end('b', last=False)
print(d.keys()) # odict_keys(['b', 'a', 'c', 'd', 'e'])
# 弹出并返回最右边（最后加入）的key-value对
print(d.popitem()[0]) # e
# 弹出并返回最左边（最先加入）的key-value对
print(d.popitem(last=False)[0]) # b
