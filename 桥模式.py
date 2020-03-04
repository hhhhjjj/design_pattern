# -*- coding: utf-8 -*-
# 适用性：
#    在以下的情况下应当使用桥梁模式：
# 1．如果一个系统需要在构件的抽象化角色和具体化角色之间增加更多的灵活性，避免在两个层次之间建立静态的联系。
# 2．设计要求实现化角色的任何改变不应当影响客户端，或者说实现化角色的改变对客户端是完全透明的。
# 3．一个构件有多于一个的抽象化角色和实现化角色，系统需要它们之间进行动态耦合。
# 4．虽然在系统中使用继承是没有问题的，但是由于抽象化角色和具体化角色需要独立变化，设计要求需要独立管理这两者。
class AbstractRoad(object):
    '''路基类'''
    car = None


class AbstractCar(object):
    '''车辆基类'''

    def run(self):
        raise NotImplementedError


class Street(AbstractRoad):
    '''市区街道'''

    def run(self):
        self.car.run()
        print("在市区街道上行驶")


class SpeedWay(AbstractRoad):
    '''高速公路'''

    def run(self):
        self.car.run()
        print("在高速公路上行驶")


class Car(AbstractCar):
    '''小汽车'''

    def run(self):
        print("小汽车在")


class Bus(AbstractCar):
    '''公共汽车'''

    def run(self):
        print("公共汽车在")


if __name__ == "__main__":
    # 小汽车在高速上行驶
    road1 = SpeedWay()
    road1.car = Car()
    road1.run()

    #
    road2 = SpeedWay()
    road2.car = Bus()
    road2.run()

    road3 = Street()
    road3.car = Bus()
    road3.run()
# 原文链接：https: // blog.csdn.net / burgess_zheng / article / details / 86762248