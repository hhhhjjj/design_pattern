# -*- coding: utf-8 -*-
import threading
class Singleton(object):
    _instance_lock = threading.Lock()
    # 在这加个线程锁

    def __init__(self):
        pass

# 先new实例化对象，然后再init
    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance