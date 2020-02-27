# -*- coding: utf-8 -*-
# 简单工厂只有一个工厂，工厂方法模式每一个产品都有相应的工厂
# 好处：增加一个运算类（例如N次方类），只需要增加运算类和相对应的工厂，两个类，不需要修改工厂类。
# 缺点：增加运算类，会修改客户端代码，工厂方法只是把简单工厂的内部逻辑判断移到了客户端进行

class ShapeFactory(object):
    '''工厂类'''

    def getShape(self):
        return self.shape_name


class Circle(ShapeFactory):

    def __init__(self):
        self.shape_name = "Circle"

    def draw(self):
        print('draw circle')


class Rectangle(ShapeFactory):
    def __init__(self):
        self.shape_name = "Retangle"

    def draw(self):
        print('draw Rectangle')


class ShapeInterfaceFactory(object):
    '''接口基类'''

    # 只要共同属性的，就创建个基类
    def create(self):
        '''把要创建的工厂对象装配进来'''
        raise NotImplementedError


class ShapeCircle(ShapeInterfaceFactory):

    def create(self):
        return Circle()


class ShapeRectangle(ShapeInterfaceFactory):
    def create(self):
        return Rectangle()


shape_interface = ShapeCircle()
obj = shape_interface.create()
print(obj.getShape())
obj.draw()

shape_interface2 = ShapeRectangle()
obj2 = shape_interface2.create()
obj2.draw()


# 原文链接：https: // blog.csdn.net / burgess_zheng / article / details / 86762248




