# как создать/запустить поток
import queue
from time import perf_counter, sleep
import threading

# def summa():
#     summ = 0
#     for i in range(100000000):
#         summ += i
#
# start = perf_counter()
# summa()
# finish = perf_counter()
# print(f'время работы {finish - start} секунд без потока')
#
# thread = threading.Thread(target=summa)
#
# start = perf_counter()
# thread.start()
# thread.join()
# finish = perf_counter()
# print(f'время работы {finish - start} секунд c потоком')


# потоки на классах/обработка исключений
# class MyThread(threading.Thread):
#     def __init__(self, num):
#         super().__init__()
#         self.num = num
#
#     def run(self):
#         try:
#             if self.num % 2 == 0:
#                 raise RuntimeError(f'Четный поток! {self.num}')
#             print(f'Поток {self.num} работает исправно!')
#             sleep(1)
#         except Exception as exc:
#             print(f'Обработано исключение! {self.num} : {exc}')
#
# threads = []
# for i in range(1,11):
#     thread = MyThread(i)
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()

# # проблемы мультипоточного программирования
# data = 0
# lock = threading.Lock()
#
# def summa():
#     global data
#     with lock:
#         for i in range(100000000):
#             data += 1
#
# t1 = threading.Thread(target=summa)
# t2 = threading.Thread(target=summa)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print(data)
# # глобальная блокировка интерпретатора
# def summa():
#     data = 0
#     for i in range(100000000):
#         data += i
#
# start = perf_counter()
# summa()
# summa()
# finish = perf_counter()
# print(f'время работы {finish - start} секунд без потока')
#
# t1 = threading.Thread(target=summa)
# t2 = threading.Thread(target=summa)
#
# start = perf_counter()
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# finish = perf_counter()
# print(f'время работы {finish - start} секунд с потоками')

# очереди
# queue.Queue - стандартная
# queue.PriorityQueue - приоритетная

# q = queue.Queue()

# def plus():
#     for i in range(1,11):
#         # q.put(f'{i} - число в очереди!')
#         print(f'Положительное число! {i}')
#         # sleep(1)
#
# def minus():
#     for i in range(1,11):
#         # q.get()
#         print(f'Отрицательное число! {-i}')
#         # q.task_done()
#
# t1 = threading.Thread(target=plus)
# t2 = threading.Thread(target=minus)
#
# start = perf_counter()
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# finish = perf_counter()
# print(f'время работы {finish - start} секунд с потоками')
