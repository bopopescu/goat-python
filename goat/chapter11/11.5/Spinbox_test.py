# coding: utf-8

from tkinter import *
# 导入ttk
from tkinter import ttk
class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()
    def initWidgets(self):
        ttk.Label(self.main, text='指定from、to、increment').pack()
        # 通过指定from_、to、increament选项创建Spinbox
        sb1 = Spinbox(self.main, from_ = 20,
            to = 100,
            increment = 5)
        sb1.pack(fill=X, expand=YES)
        ttk.Label(self.main, text='指定values').pack()
        # 通过指定values选项创建Spinbox
        self.sb2 = Spinbox(self.main, 
            values=('Python', 'Swift', 'Kotlin', 'Ruby'),
            command = self.press) # 通过command绑定事件处理方法
        self.sb2.pack(fill=X, expand=YES)
        ttk.Label(self.main, text='绑定变量').pack()
        self.intVar = IntVar()
        # 通过指定values选项创建Spinbox，并为之绑定变量
        sb3 = Spinbox(self.main, 
            values=list(range(20, 100, 4)),
            textvariable = self.intVar, # 绑定变量
            command = self.press)
        sb3.pack(fill=X, expand=YES)
        self.intVar.set(33) # 通过变量改变Spinbox的值
    def press(self):
        print(self.sb2.get())
root = Tk()
root.title("Spinbox测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
