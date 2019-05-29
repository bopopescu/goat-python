# coding: utf-8

import re
# 对模式中特殊字符进行转义
print(re.escape(r'www.crazyit.org is good, i love it!'))
# 输出：www\.crazyit\.org\ is\ good\,\ i\ love\ it\!
print(re.escape(r'A-Zand0-9?'))
# 输出：A\-Zand0\-9\?
