'''
Обработать строку ospf_route и вывести информацию в виде:
Protocol:               OSPF
Prefix:                 10.0.24.0/24
AD/Metric:              110/41
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0
В разделе Форматирование строк добавились примеры, которые помогут с отображением вывода столбцами.
'''


ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

s = ospf_route.split()
#print(s)
s_protocol = s[0].replace('O','OSPF')
s_prefix  = s[1]
s_metric = s[2]
s_metric = s_metric[1:-1]
s_next_hop = s[4]
s_next_hop = s_next_hop[:-1]
s_last_upd = s[5]
s_last_upd = s_last_upd[:-1]
s_interface = s[6]

print ("Protocol:",'{:>25}'.format(s_protocol))
print ('Prefix:','{:>35}'.format(s_prefix))
print ('AD/Metric:','{:>26}'.format(s_metric))
print ('Next-Hop:','{:>30}'.format(s_next_hop))
print ('Last update:','{:>23}'.format(s_last_upd))
print ('Outbound Interface:','{:>26}'.format(s_interface ))

ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

info  = ['Protocol:', 'Prefix:','AD/Metric:','Next-Hop:','Last update:','Outbound Interface:']

s = ospf_route.split()
print(s)
print(info)