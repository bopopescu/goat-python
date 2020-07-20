# coding: utf-8

# 将tkinter写成Tkinter可兼容Python 2.x
from tkinter import *
class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()
    def initWidgets(self):
        self.show = Label(self.main, width=30, bg='white', font=('times', 20))
        self.show.pack()
        bn = Button(self.main, text='单击我或双击我')
        bn.pack(fill=BOTH, expand=YES)
        # 为左键单击事件绑定处理方法
        bn.bind('<Button-1>', self.one)
        # 为左键双击事件绑定处理方法
        bn.bind('<Double-1>', self.double) 
    def one(self, event):
        self.show['text'] = "左键单击:%s" % event.widget['text']
    def double(self, event):
        print("左键双击击, 退出程序:", event.widget['text']) 
        import sys; sys.exit() 
root = Tk()
root.title('简单绑定')
App(root)
root.mainloop()
