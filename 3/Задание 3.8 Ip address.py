'''

Конвертировать в двоичный формат, указать сколько цифр должно быть в отображении числа и дополнить недостающее нулями:+

In [10]: '{:08b}'.format(10)
Out[10]: '00001010'
Аналогичный результат можно получить с помощью метода zfill:
In [11]: bin(10)[2:].zfill(8)
Out[11]: '00001010'

Задание 3.8

Преобразовать IP-адрес (переменная IP) в двоичный формат и вывести вывод столбцами, таким образом:
первой строкой должны идти десятичные значения байтов
второй строкой двоичные значения
Вывод должен быть упорядочен также, как в примере:
столбцами
ширина столбца 10 символов
Пример вывода:
10        1         1         1
00001010  00000001  00000001  00000001
IP = '192.168.3.1'
'''
IP = '192.168.3.1'
ip_list = IP.split('.')

list_bin = [bin(int(i)+256)[3:] for i in ip_list]
actet0,actet1,actet2,actet3 = list_bin

print(''.join('{:10}'.format(x) for x in ip_list))
print ("%0s %9s %9s %9s" % (actet0,actet1,actet2,actet3))

print("_______________________________________")
print(''.join('{:10}'.format(x) for x in ip_list))
print(''.join('{:08b}  '.format(int(x)) for x in ip_list))

'''
IP = '192.168.3.1'
ip_dec = IP.split('.')
print ("{:10}{:10}{:10}{:10}".format(ip_dec[0], ip_dec[1], ip_dec[2], ip_dec[3]))
print ("{:08b}  {:08b}  {:08b}  {:08b}".format(int(ip_dec[0]), int(ip_dec[1]), int(ip_dec[2]), int(ip_dec[3])))

P = '192.168.3.1'
L = P.split('.')
print(''.join('{:10}'.format(x) for x in L))
print(''.join('{:08b}  '.format(int(x)) for x in L))
'''
#Преобразование в двоичную систему
print('{:08b}' .format(222))