# введение
# def names():
#     print('Марина')
#
# print(names.__name__)
#
# func = names
# print(func.__name__)


# def add(numbers):
#     res = 0
#     for number in numbers:
#         res += number
#     return res
#
# def multi(numbers):
#     res = 1
#     for number in numbers:
#         res *= number
#     return res
#
# def process(numbers, func):
#     result = func(numbers)
#     print(f'Получилось {result}!')
#
# numbers = [1,2,3,4,5,6]
#
# process(numbers=numbers, func=multi)
# process(numbers, add)


# списковая сборка
# numbers = [1,2,3,4,5,6]

# result = [i**2 for i in numbers]
# print(result)

# генераторные сборки
# numbers = [1,2,3,4,5,6]
#
# result = (i**2 for i in numbers)
# print(result)
# for elem in result:
#     print(elem)
#
# print(result)
# for elem in result:
#     print(elem)


# лямбда функции
# def add(a,b):
#     return a+b
#
# res = lambda a, b: a + b
# print(res(51, 110))

# создание собственного итератора
# class Iterator:
#     def __init__(self):
#         self.first = 'первый'
#         self.second = 'второй'
#         self.third = 'третий'
#         self.i = 0
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         self.i += 1
#         if self.i == 1:
#             return self.first
#         elif self.i == 2:
#             return self.second
#         elif self.i == 3:
#             return self.third
#         raise StopIteration()
#
# obj = Iterator()
# print(obj)
# for elem in obj:
#     print(elem)


# декораторы
# def up(func):
#     def wrapper():
#         res = func()
#         new_res = res.upper()
#         return new_res
#     return wrapper
#
# @up
# def greet():
#     return 'helloooo!'
#
# print(greet())
