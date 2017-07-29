access_template = ['switchport mode access',
                   'switchport access vlan %d',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print ('\n'.join(access_template) % 5)

'''
D:\Study\Python\Projects\Python for network engener\4\examples>python access_template.py
switchport mode access
switchport access vlan 5
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
'''
help(list.index)