#!/usr/bin/python3

from get_comp_ip import get_comp_ip

#info = get_comp_ip('10.127.193.138', 'root', password='cisco123')
info = get_comp_ip('10.127.193.241', 'root', password='cisco123')
#for i in range(1, 100):
#print(info.return_complist())
if info.check_if_lb():
    print("Yup this a lb")
    
if info.check_if_HA():
    print("this is running")
    print(info.return_complist)

#print(info.)
#Aswathi = 6 to 15
#naveen = 17 to 24
