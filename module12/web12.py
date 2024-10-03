# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# def mul(a,b):
#     return a*b
#
# def div(a,b):
#     return a/b
#
# if __name__ == '__main__':
#     print(add(100,123))

import logging

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b
    # try:
    #     a/b
    #     logging.info(f'Успешное деление {a}/{b}')
    #     return a/b
    # except ZeroDivisionError:
    #     logging.error('Исключение: деление на 0', exc_info=True)
#         return 0

if __name__ == '__main__':
    logging.debug('gf')
    logging.info('j')
    logging.warning('f')
    logging.error('f')
    logging.critical('a')
    # logging.basicConfig(level=logging.INFO, filemode='w', filename='py.log',
    #                     format='%(asctime)s | %(levelname)s | %(message)s')
    # print(div(3,4))
    # print(div(3,0))
