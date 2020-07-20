# coding: utf-8

from tkinter import *
# 导入ttk
from tkinter import ttk
class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()
    def initWidgets(self):
        # 创建一个Label组件
        ttk.Label(self.main, text='选择您喜欢的图书:')\
            .pack(fill=BOTH, expand=YES)
        self.intVar = IntVar()
        # 定义元组
        books = ('疯狂Kotlin讲义', '疯狂Python讲义',
            '疯狂Swift讲义',  '疯狂Java讲义')
        i = 1
        # 采用循环创建多个Radiobutton
        for book in books:
            ttk.Radiobutton(self.main, 
                text = book,
                variable = self.intVar, # 将Radiobutton绑定到self.intVar变量
                command = self.change, # 将选中事件绑定到self.change方法
                value=i).pack(anchor=W)
            i += 1
        # 设置Radiobutton绑定的变量的值为2，
        # 则选中value为2的Radiobutton
        self.intVar.set(2)
    def change(self):
        from tkinter import messagebox
        # 通过Radiobutton绑定变量获取选中的单选框
        messagebox.showinfo(title=None, message=self.intVar.get() )
root = Tk()
root.title("Radiobutton测试")
App(root)
root.mainloop()
