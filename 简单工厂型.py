# -*- coding: utf-8 -*-
# 在工厂模式中，不暴露创建逻辑，通过接口来指向创建的对象
# 原文链接：https: // blog.csdn.net / burgess_zheng / article / details / 86762248
class Shape(object):
    '''
    父类
    '''

    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    '''
    Shape子类
    '''

    def draw(self):
        print('draw circle')


class Rectangle(Shape):
    '''
    Shape的子类
    '''

    def draw(self):
        print('draw Rectangle')


class ShapeFactory(object):
    '''
    工厂模式：暴露给用户去调用的，
    用户可通过该类进行选择Shape的子类进行实例化
    '''

    def create(self, shape):
        if shape == 'Circle':
            return Circle()
        # 如果想增加运算类的话，在这还需要修改，违反了开闭原则
        elif shape == 'Rectangle':
            return Rectangle()
        else:
            return None

fac = ShapeFactory() #实例化工厂类
obj = fac.create('Circle') #实例化Shape的Circle子类
obj.draw()
# 最后显示的是circle的draw
