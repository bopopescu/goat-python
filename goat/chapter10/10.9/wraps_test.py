# coding: utf-8

from functools import wraps

def fk_decorator(f):
    # 让wrapper函数看上去就像f函数
    @wraps(f)
    def wrapper(*args, **kwds):
        print('调用被装饰函数')
        return f(*args, **kwds)
    return wrapper
@fk_decorator
def test():
    """test函数的说明信息"""
    print('执行test函数')
test()
#print(test.__name__)
#print(test.__doc__)
