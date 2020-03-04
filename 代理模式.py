# -*- coding: utf-8 -*-
# 在直接访问对象时带来的问题，比如说：要访问的对象在远程的机器上。
# 在面向对象系统中，有些对象由于某些原因（比如对象创建开销很大，或者某些操作需要安全控制，或者需要进程外的访问），
# 直接访问会给使用者或者系统结构带来很多麻烦，我们可以在访问此对象时加上一个对此对象的访问层。

# 其实就是Windows快捷方式
class sender_base:
    def __init__(self):
        pass

    def send_something(self, something):
        pass


class send_class(sender_base):
    def __init__(self, receiver):
        self.receiver = receiver

    def send_something(self, something):
        print("SEND " + something + ' TO ' + self.receiver.name)


class agent_class(sender_base):
    def __init__(self, receiver):
        self.send_obj = send_class(receiver)

    def send_something(self, something):
        self.send_obj.send_something(something)
# 代理模式
# 应用特性：需要在通信双方中间需要一些特殊的中间操作时引用，多加一个中间控制层。
# 结构特性：建立一个中间类，创建一个对象，接收一个对象，然后把两者联通起来

class receive_class:
    def __init__(self, someone):
        self.name = someone


if '__main__' == __name__:
    receiver = receive_class('Burgess')
    agent = agent_class(receiver)
    agent.send_something('agentinfo')

    print(receiver.__class__)
    print(agent.__class__)



# 原文链接：https: // blog.csdn.net / burgess_zheng / article / details / 86762248