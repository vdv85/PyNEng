'''
Задание 3.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).
MAC = "AAAA:BBBB:CCCC"
'''

MAC = "AAAA:BBBB:CCCC"
MAC = MAC.replace(':','')
print(MAC)