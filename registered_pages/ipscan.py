import nmap

import streamlit as lit

from getmac import get_mac_address


scanner = nmap.PortScanner()

def ipscanner_py():
    count = 0

    scanner.scan(hosts='192.168.1.0/24', arguments='-sn')
    hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
    for host, status in hosts_list:
        devices=('{0}:{1}'.format(host, status))
        print('{0}:{1}'.format(host, status))
        print(devices)
        count += 1

    enter=input("Are all ",count," devices yours? (press any key to see more details): \n\n")
    print(count)
  
    #print(output)


    #audit=input("This list shows you the unique number connected to each device you have on your network. \nSee how many you can identify \n\n")



def ipscanner_lit():
    
    if "gateway" not in lit.session_state:
        lit.session_state["gateway"]= ""

    gateway = lit.session_state["gateway"]



    count = 0


    scanner.scan(hosts="192.168.1.1/24", arguments='-sn')
    hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
    for host, status in hosts_list:
        devices=('{0}:{1}'.format(host, status))
        #lit.write('{0}:{1}'.format(host, status))
        lit.write(devices)
        count += 1



    