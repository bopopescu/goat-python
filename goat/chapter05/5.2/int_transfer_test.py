# coding: utf-8

def swap(a , b) :
    # 下面代码实现a、b变量的值交换
    a, b = b, a
    print("swap函数里，a的值是", \
        a, "；b的值是", b)
a = 6
b = 9
swap(a , b)
print("交换结束后，变量a的值是", \
    a , "；变量b的值是", b)
