# coding: utf-8

# 一个简单的for循环
for i in range(0, 3 ) :
    print("i的值是: ", i)
    if i == 1 :
        # 忽略本次循环的剩下语句
        continue
    print("continue后的输出语句")