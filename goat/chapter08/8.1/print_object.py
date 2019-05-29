# coding: utf-8

class Item:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
# 创建一个Item对象，将之赋给im变量
im = Item('鼠标', 29.8)
# 打印im所引用的Item对象
print(im)

im_str = im.__repr__() + ""
print(im_str)