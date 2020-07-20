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
        ttk.Label(self.main, text='选择您喜欢的兵种:')\
            .pack(fill=BOTH, expand=YES)
        self.intVar = IntVar()
        # 定义元组
        races = ('z.png', 'p.pNg','t.png')
        raceNames = ('虫族', '神族','人族')
        i = 1
        # 采用循环创建多个Radiobutton
        for rc in races:
            bm = PhotoImage(file = 'images/' + rc)
            r = ttk.Radiobutton(self.main, 
                image = bm,
                text = raceNames[i - 1],
                compound = RIGHT, # 图片在文字右边
                variable = self.intVar, # 将Radiobutton绑定到self.intVar变量
                command = self.change, # 将选中事件绑定到self.change方法
                value=i)
            r.bm = bm
            r.pack(anchor=W)
            i += 1
        # 设置默认选中value为2的单选按钮
        self.intVar.set(2)
    def change(self): pass
root = Tk()
root.title("Radiobutton测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
