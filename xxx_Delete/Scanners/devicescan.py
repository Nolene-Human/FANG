# -- Scanning and Identifying all devices connected to the network

# @ TO DO
# - Split data in more readable output


import nmap
nm = nmap.PortScanner()
import streamlit as lit

# -- find a way to save network -- #

def listdevices_py():
    sniffing=nm.scan(hosts="192.168.1.0/24", arguments='-n -sP -PE')
    print("this is the hostname: " ,sniffing)

    lines=sniffing.split("}},")

    for ft in lines:
        print(ft)


def listdevices_lit():
    sniffing=nm.scan(hosts="192.168.1.0/24", arguments='-n -sP -PE')
    lit.markdown("this is the hostname: " ,sniffing)


    