# coding: utf-8

name = 'Charlie'
def test ():
    # 直接访问name全局变量
    print(globals()['name'])  # Charlie
    name = '孙悟空'
test()
print(name)  # Charlie
