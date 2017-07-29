'''
Задание 3.3

Получить из строки CONFIG список VLAN вида ['1', '3', '10', '20', '30', '100'].
'''

CONFIG = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlan = CONFIG.split()
vlan = vlan[-1].split(",")
print(vlan)




