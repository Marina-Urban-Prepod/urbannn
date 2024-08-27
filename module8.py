#1
# a = 'Python'
# code = []
# for i in a:
#     code.append(ord(i))
# print(code)
#
# s = ''
# for i in code:
#     s += chr(i)
# print(s)

# for i in range(1000):
#     print(chr(i))
#
# print(hex(ord('q')))
# b = b'\x71'
# print(b)


#2
# import os
# text = open('text.txt', 'r')
# print(text.read())
# text.close()

# text = open('text.txt', 'w')
# text.write('Шли годы.')
# text.close()

# text = open('text.txt', 'a')
# text.write('\nШли годы. Бурь порыв мятежный')
# text.close()

#3
# text = open('text.txt', 'a', encoding='utf-8')
# text.seek(10)
# print(text.tell())
#
# print(text.readable())
# print(text.writable())
# print(text.seekable())

# #4
# text = 'text.txt'
# with open(text, encoding='utf-8') as file:
#     for line in file:
#         for char in line:
#             print(f'{char} - символ')
