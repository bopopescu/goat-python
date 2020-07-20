# coding: utf-8

from tkinter import *
# 导入ttk
from tkinter import ttk

class App:
    def __init__(self, main):
        self.main = main
        self.initWidgets()
    def initWidgets(self):
        # 创建Style
        style = ttk.Style()
        style.configure("fkit.TPanedwindow",
            background='darkgray', relief=RAISED)
        # 创建Panedwindow组件，通过style属性配置分隔线
        pwindow = ttk.Panedwindow(self.main,
            orient=HORIZONTAL, style="fkit.TPanedwindow")
        pwindow.pack(fill=BOTH, expand=YES)
        left = ttk.Label(pwindow, text="左边标签", background='pink')
        pwindow.add(left)
        # 创建第二个Panedwindow组件，该组件的方向为垂直方向
        rightwindow = PanedWindow(pwindow, orient=VERTICAL)
        pwindow.add(rightwindow)
        top = Label(rightwindow, text="右上标签", background='lightgreen')
        rightwindow.add(top)  
        bottom = Label(rightwindow, text="右下标签", background='lightblue')
        rightwindow.add(bottom)  
root = Tk()
root.title("Panedwindow测试")
App(root)
root.mainloop()
