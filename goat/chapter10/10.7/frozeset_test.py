# coding: utf-8

s = set()
frozen_s = frozenset('Kotlin')
# 为set集合添加frozenset
s.add(frozen_s)
print('s集合的元素：', s)
sub_s = {'Python'}
# 为set集合添加普通set集合，程序报错
s.add(sub_s) 