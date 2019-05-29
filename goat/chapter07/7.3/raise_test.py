# coding: utf-8

import traceback
def main():
    try:
        # 使用try...except来捕捉异常
        # 此时即使程序出现异常，也不会传播给main函数
        mtd(3)
    except Exception as e:
        print('程序出现异常:', e)
#        help(e.with_traceback)
        traceback.print_exc()
#        e.with_traceback(e)
    # 不使用try...except捕捉异常，异常会传播出来导致程序中止
    mtd(3)
def mtd(a):
    if a > 0:
        raise ValueError("a的值大于0，不符合要求")
main()