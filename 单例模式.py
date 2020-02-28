# -*- coding: utf-8 -*-
# 保证一个类仅有一个实例，并提供一个访问它的全局访问点。
# 当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时。
# 当这个唯一实例应该是通过子类化可扩展的，
# 并且客户应该无需更改代码就能使用一个扩展的实例时。


# 实现__new__方法
# 并在将一个类的实例绑定到类变量_instance上,
# 如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
# 如果cls._instance不为None,直接返回cls._instance
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            # cls = a = MyClass('Burgess')
            # 判断是否有a该实例存在,前面是否已经有人实例过，如果内存没有该实例...往下执行
            # 需要注明该父类的内存空间内最多允许相同名字子类的实例对象存在1个（不可多个）

            orig = super(Singleton, cls)  # farther class
            cls._instance = orig.__new__(cls)
            # orig =让cls继承指定的父类 Singleton
            # cls._instance = 创建了MyClass('Burgess') 该实例
            # 这两句相当于外面的 a= MyClass('Burgess')
        return cls._instance  # 具体的实例


class MyClass(Singleton):
    def __init__(self, name):
        self.name = name


class Nana(Singleton):
    def __init__(self, name):
        self.name = name


a = MyClass("Burgess")
print(a.name)
b = MyClass("Crystal")
# 在这的时候a的name也被改了，因为这只是一个实例
print(a.name)
print(b.name)
b.name = 'xx'
# 在这的时候a的name也被改了
print(a.name)
print(b.name)
# 原文链接：https: // blog.csdn.net / burgess_zheng / article / details / 86762248

