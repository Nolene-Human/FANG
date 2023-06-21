import streamlit as lit
import nmap   
import Firebase.firebaseconfig

import uuid
import socket
import subprocess


def findhostdetails():
      # -- get the devices Ip address (Wlan) using subprocess -- #
    result=subprocess.run('ipconfig',stdout=subprocess.PIPE,text=True).stdout.lower()
    scan=0
    for i in result.split('\n'):
        if 'wireless' in i: scan=1
        if scan:
            if 'ipv4' in i: return i.split(':')[1].strip()



def thisdevice():
    mac_addr = (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
        for elements in range(0,2*6,2)][::-1]))
   
    try:
        hostname = socket.gethostname()

    except:
        lit.write("Unable to get Hostname and IP")

    yourdevice={"ip":findhostdetails(),"mac":mac_addr,"manufacturer":"","name":hostname}

    return yourdevice


saved_device_list=[]
new_list_devices_nmap=[]
full_list_devices_nmap=[]

def devices_scan():

    auth=Firebase.firebaseconfig.firebase_auth()    
    database=Firebase.firebaseconfig.firebase_database()
    
    user=auth.sign_in_with_email_and_password('test1@gmail.com','D4nc3r$')

    tab1,tab2=lit.tabs(['Saved Devices','Scan Network'])

    # UX / UI creating columns to return results into rows            
    # Column Headers                                
    # UX/UI for scanning Network 


    with tab1:
        lit.write("This is your device : ", thisdevice())


        ip_s,mac_s,manuf_s,category_s =lit.columns(4)
        ip_s.markdown("**IP Address**")
        mac_s.markdown("**MAC Address**")
        manuf_s.markdown("**Manufacturer**")
        category_s.markdown("**Category**")
        try:
            get_your_devices=database.child(user['localId']).child('Devices').get()
            for your_devices in get_your_devices.each():
                s_result=your_devices.val()
                ip_s.write(s_result["ip"])
                saved_mac=mac_s.write(s_result["mac"])
                manuf_s.write(s_result["manufacturer"])
                category_s.write(s_result["name"])

        except:
            lit.warning("No devices saved to your database")

    with tab2:
        one,two,three=lit.columns(3)
        full_scan=one.button("Full Scan Saved and New")
        scan=three.button("Scan for new devices")
        
        # -- UI/UX Columns and Headers
        ip_sc,mac_sc,manuf_sc,category_sc =lit.columns(4)
        ip_sc.markdown("**IP Address**")
        mac_sc.markdown("**MAC Address**")
        manuf_sc.markdown("**Manufacturer**")
        category_sc.markdown("**Category**")
        
        # -- Running full scan and calling all devices on the network
        if full_scan:
            new_list_devices_nmap.clear()
            full_list_devices_nmap.clear()

            lit.write("[Lookup the Mac address to see who is the manufacturer](https://mac.lc)")
            new=nmap.PortScanner()         
            
            new.scan(hosts='192.168.1.0/24', arguments='-sn')
                 
            for host in new.all_hosts():
                
                if 'mac' in new[host]['addresses']:
                    mac_address = new[host]["addresses"]["mac"]
                    manufacturer = new[host]["vendor"].get(mac_address, "Unknown")

                    ip_sc.write(host)
                    mac_sc.write(mac_address)
                    manuf_sc.write(manufacturer)

                    devices_nmap={"ip":host,"mac":mac_address,"manufacturer":manufacturer,"name":""}
                    full_list_devices_nmap.append(devices_nmap)
            

        if scan:
            new_list_devices_nmap.clear()
            full_list_devices_nmap.clear()
            
            lit.write("[Lookup the Mac address to see who is the manufacturer](https://mac.lc)")
            new=nmap.PortScanner()         
            
            new.scan(hosts='192.168.1.0/24', arguments='-sn')
                 
            for host in new.all_hosts():
                
                if 'mac' in new[host]['addresses']:
                    mac_address = new[host]["addresses"]["mac"]
                    manufacturer = new[host]["vendor"].get(mac_address, "Unknown")
                    device_name="New"

                    ip_sc.write(host)
                    mac_sc.write(mac_address)
                    manuf_sc.write(manufacturer)
                    category_sc.write(device_name)
                        
                    devices_nmap={"ip":host,"mac":mac_address,"manufacturer":manufacturer,"name":device_name}
                    new_list_devices_nmap.append(devices_nmap)
                 

                
