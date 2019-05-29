# coding: utf-8

from collections import deque
stack = deque(('Kotlin', 'Python'))
# 元素入栈
stack.append('Erlang')
stack.append('Swift')
print('stack中的元素：' , stack)
# 元素出栈，后添加的元素先出栈
print(stack.pop())
print(stack.pop())
print(stack)