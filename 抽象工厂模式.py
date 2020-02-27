# -*- coding: utf-8 -*-
# 抽象工厂模式与工厂方法模式的最大区别就在于，工厂方法模式针对的是一个产品等级结构；而抽象工厂模式则需要面对多个产品等级结构。
# 　　在学习抽象工厂具体实例之前，应该明白两个重要的概念：产品族和产品等级。
# 所谓产品族，是指位于不同产品等级结构中，功能相关联的产品组成的家族。
# 比如AMD的主板、芯片组、CPU组成一个家族，Intel的主板、芯片组、CPU组成一个家族。
# 而这两个家族都来自于三个产品等级：主板、芯片组、CPU。
# 原文链接：https://blog.csdn.net/burgess_zheng/article/details/86762248
# 切换产品族的时候，只要提供不同的抽象工厂实现就可以了
# 抽象工厂和工厂模式的对比区别：
# 抽象工厂：规定死了，依赖限制，假上面实验，你用intel的机器只能配置intel的CPU不能配置AMD的CPU（由各自的工厂指定自己的产品生产品牌）
# 工厂模式：不是固定死的，举例：你可使用intel的机器配置AMD的CPU
class AbstractFactory(object):
    computer_name = ''

    def createCpu(self):
        pass

    def createMainboard(self):
        pass


class IntelFactory(AbstractFactory):
    computer_name = 'Intel I7-series computer '

    def createCpu(self):
        return IntelCpu('I7-6500')

    def createMainboard(self):
        return IntelMainBoard('Intel-6000')


class AmdFactory(AbstractFactory):
    computer_name = 'Amd 4 computer '

    def createCpu(self):
        return AmdCpu('amd444')

    def createMainboard(self):
        return AmdMainBoard('AMD-4000')


class AbstractCpu(object):
    series_name = ''
    instructions = ''
    arch = ''


class IntelCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AmdCpu(AbstractCpu):
    def __init__(self, series):
        self.series_name = series


class AbstractMainboard(object):
    series_name = ''


class IntelMainBoard(AbstractMainboard):
    def __init__(self, series):
        self.series_name = series


class AmdMainBoard(AbstractMainboard):
    def __init__(self, series):
        self.series_name = series


class ComputerEngineer(object):

    def makeComputer(self, factory_obj):
        self.prepareHardwares(factory_obj)

    def prepareHardwares(self, factory_obj):
        self.cpu = factory_obj.createCpu()
        self.mainboard = factory_obj.createMainboard()

        info = '''------- computer [%s] info:
    cpu: %s
    mainboard: %s
 -------- End --------
        ''' % (factory_obj.computer_name, self.cpu.series_name, self.mainboard.series_name)
        print(info)


if __name__ == "__main__":
    engineer = ComputerEngineer()  # 装机工程师

    intel_factory = IntelFactory()  # intel工厂
    engineer.makeComputer(intel_factory)

    amd_factory = AmdFactory()  # adm工厂
    engineer.makeComputer(amd_factory)


