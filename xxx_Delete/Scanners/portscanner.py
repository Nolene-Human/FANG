
import streamlit as lit
import nmap


scanner = nmap.PortScanner()

def portscanner(ip_addr):
    scanner.scan(ip_addr,'1-1024','-v -sS')
    lit.write("Open Ports on TCP ",scanner[ip_addr]['tcp'].keys())
 
    # -- Scan UDP open port on Device -- #
    scanner.scan(ip_addr,'1-1024','-v -sU')
    lit.write("Open Ports on UDP ",scanner[ip_addr]['udp'].keys())  