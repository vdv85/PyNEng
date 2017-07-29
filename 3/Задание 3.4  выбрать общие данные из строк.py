'''
Задание 3.4

Из строк command1 и command2 получить список VLAN, которые есть и в команде command1 и в команде command2. Не использовать для решения задачи циклы, оператор if.
Для данного примера, результатом должен быть список: [1, 3, 100]


command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"
'''

command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"
c1 = command1.split()
c2 = command2.split()
c1vlan = c1[-1].split(",")
c2vlan = c2[-1].split(",")
print(c1vlan)
print(c2vlan)
vlan = tuple(c1vlan&c2vlan)
print(vlan)
