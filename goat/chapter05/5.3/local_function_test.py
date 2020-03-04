# coding: utf-8

# 定义函数，该函数会包含局部函数
vdef get_math_func(type, nn) :
    # 定义一个计算平方的局部函数
    def square(n) :  # ①
        return n * n
    # 定义一个计算立方的局部函数
    def cube(n) :  # ②
        return n * n * n
    # 定义一个计算阶乘的局部函数
    def factorial(n) :   # ③
        result = 1
        for index in range(2, n + 1) :
            result *= index
        return result
    # 调用局部函数
    if type == "square" :
        return square(nn)
    elif type == "cube":
        return cube(nn)
    else:
        return factorial(nn)
print(get_math_func("square", 3)) # 输出9
print(get_math_func("cube", 3)) # 输出27
print(get_math_func("", 3)) # 输出6
