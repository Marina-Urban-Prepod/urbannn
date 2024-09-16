# https://pypi.org/

import requests

some_str = 'sdfghjkl;'
some_n = 1021029
some_l = [some_str, some_n]

def func(a,b):
    return a + b

class SClass():
    def __init__(self):
        self.attr1 = 1212

    def method(self, val):
        self.attr1 = val
        print(self.attr1)

obj1 = SClass()

qq = func

# print(requests.__name__)
# print(SClass.__name__)
# print(qq.__name__)
#
# print(some_n.__name__)

# print(type(func))
# print(type(requests))
# print(type(some_l))

# print(hasattr(obj1, 'attr1'))
# print(hasattr(obj1, 'attr2'))

# print(getattr(obj1, 'attr1'))
# print(getattr(obj1, 'attr2', 'ошибочка'))

# print(callable(obj1.attr1))
# print(callable(func))
# print(callable(some_n))

# print(isinstance(some_l, list))
# print(isinstance(some_l, str))


# import sys
# 
# # путь к интерпретатору
# print(sys.executable)
# 
# # операционка
# print(sys.platform)
# 
# # версия питона
# print(sys.version)
# print(sys.version_info)
