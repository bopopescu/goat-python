# coding: utf-8

def foo ():
    # 局部变量name
    name = 'Charlie'
    def bar ():
        nonlocal name
        # 访问bar函数所在的foo函数的name局部变量
        print(name) # Charlie
        name = '孙悟空'
    bar()
foo()