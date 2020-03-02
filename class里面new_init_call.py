# -*- coding: utf-8 -*-
# 实例化一个类的时候，最先被调用的是new，然后是init方法
class A:
    def __init__(self):
        # init负责对象的初始化
        print('__init__')
        print(self)
        super(A, self).__init__()
    # 确保父类被正确的初始化了

    def __new__(cls):
        print('__new__')
        self = super(A, cls).__new__(cls)
        print(self)
        return self
    # new的返回值就是类的实例对象self，如果new不返回值，那么init将不会得到调用
    # 要实现单例模式就用new来
# class BaseController(object):
#     _singleton = None
#     def __new__(cls, *a, **k):
#         if not cls._singleton:
#             cls._singleton = object.__new__(cls, *a, **k)
#         return cls._singleton

if __name__ == '__main__':
    A()

# 还有个call方法，将实例变成可调用对象，像函数一样调用
# a = A()
# # 如果A里面有call的话
# a()