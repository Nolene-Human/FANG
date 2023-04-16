import streamlit as lit
import nmap   

def scan_network_devices():
    #https://blog.streamlit.io/editable-dataframes-are-here/
            #https://medium.com/codefile/customizing-streamlit-columns-4bfd58fcb7c9
       
        with lit.expander("Block Device"):
            lit.write("How to remove a device from your network")
        scan = lit.checkbox("Scan for list of devices conntect to the Newtork")
        
        nm = nmap.PortScanner()
        if scan:
            lit.write("List of Devices on your network")
            nm.scan(hosts='192.168.1.0/24', arguments='-sn')
                    
            for host in nm.all_hosts():
                if 'mac' in nm[host]['addresses']:
                    mac_address = nm[host]["addresses"]["mac"]
                    manufacturer = nm[host]["vendor"].get(mac_address, "Unknown")
                    lit.write("IP Address: {}, MAC Address: {}, Manufacturer: {}".format(host, mac_address, manufacturer))