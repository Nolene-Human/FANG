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


def scapy_scan():
    import scapy.all as s 
    Scapy_scan=lit.checkbox('Scapy Scan')
    save_devices=lit.checkbox("save to database")

    list_devices=[]

    if Scapy_scan:
        answered_list=s.arping("192.168.1.0/24")
                         
        # iterate through the result and add each host to the dictionary
        for sent, received in answered_list[0].res:
            ip=received.psrc
            mac=received.hwsrc
            device_name="New"
            devices={"ip":ip,"mac":mac,"name":device_name}
            list_devices.append(devices)
            if save_devices:
                database.child(user['localId']).child('Devices').push(devices)
                              
                with ip_col:
                    lit.write(ip)
                with mac_col:
                    lit.write(mac)
                with name_col:
                    lit.write(device_name)
                         
    #lit.json(list_devices)