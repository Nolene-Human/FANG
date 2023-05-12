
import streamlit as lit

import uuid
import socket
import subprocess


def hostdetails_py() :
    # -- get the devices mac address and print for user using uuid
    print("Details of this machine is ")
    print("Mac Address : ") 
    print(':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
    for elements in range(0,2*6,2)][::-1]))

    # -- get the devices mac address and print for user using socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
        
    print("Your Computer Name is : " + hostname)
    print("Your Computer IP Address is : " + IPAddr)

    result=subprocess.run('ipconfig',stdout=subprocess.PIPE,text=True).stdout.lower()
    scan=0
    for i in result.split('\n'):
        if 'wireless' in i: scan=1
        if scan:
            if 'ipv4' in i: return i.split(':')[1].strip()

    print (result)

def hostdetails_lit() :
    # -- get the devices mac address and print for user using uuid
    lit.header("Details of this machine is ")
    lit.write("Mac Address : " + ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
    for elements in range(0,2*6,2)][::-1]))

    # -- get the devices mac address and print for user using socket -- #
    hostname = socket.gethostname()   
    lit.write("Your Computer Name is : " + hostname)
    

def ip_address_lit() :
    # -- get the devices Ip address (Wlan) using subprocess -- #
    result=subprocess.run('ipconfig',stdout=subprocess.PIPE,text=True).stdout.lower()
    scan=0
    for i in result.split('\n'):
        if 'wireless' in i: scan=1
        if scan:
            if 'ipv4' in i: return i.split(':')[1].strip()
        
    