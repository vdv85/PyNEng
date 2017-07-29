info = ["Protocol:, Prefix:, AD/Metric:, Next-Hop:, Last update:, Outbound Interface:"]
ospf_route = ["OSPF, 10.0.24.0/24, 110/41, 10.0.13.3, 3d18h, FastEthernet0/0"]
print %-15s %-15s % (info, ospf_route)