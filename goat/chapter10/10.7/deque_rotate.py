# coding: utf-8

from collections import deque
q = deque(range(5))
print('q中的元素：' , q)
# 执行旋转，使之首尾相连
q.rotate()
print('q中的元素：' , q)
# 再次执行旋转，使之首尾相连
q.rotate()
print('q中的元素：' , q)