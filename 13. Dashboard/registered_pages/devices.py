import streamlit as lit
import nmap   
import Firebase.firebaseconfig

import pandas as pd

import uuid
import socket
import subprocess



## ______________________________________________________________________________________________________________________##

# -- get your device Ip address (Wlan) using subprocess -- #
def findhostdetails():
      
    result=subprocess.run('ipconfig',stdout=subprocess.PIPE,text=True).stdout.lower()
    scan=0
    for i in result.split('\n'):
        if 'wireless' in i: scan=1
        if scan:
            if 'ipv4' in i: return i.split(':')[1].strip()


# -- get your device mac address and name -- #
def thisdevice():
    mac_addr = (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
        for elements in range(0,2*6,2)][::-1]))
   
    try:
        hostname = socket.gethostname()

    except:
        lit.write("Unable to get Hostname and IP")

    # -- ADDING ALL DATA INTO A LIST TO CALL IN SCANNED DEVICES #
    yourdevice={"ip":findhostdetails(),"mac":mac_addr,"manufacturer":"","name":hostname}

    return yourdevice

## ______________________________________________________________________________________________________________________##

def segment():
    auth=Firebase.firebaseconfig.firebase_auth()    
    database=Firebase.firebaseconfig.firebase_database()
    
    user=auth.sign_in_with_email_and_password('test1@gmail.com','D4nc3r$')
    edit_devices=database.child(user['localId']).child('Devices').get()
    
    show_dataframe_devices=[]
    
    save_devices=lit.button("Save Devices")

    for device in edit_devices.each():
            
            val_result=device.val()

            ip_result=val_result["ip"]
            mac_result=val_result["mac"]
            man_result=val_result["manufacturer"]
            cat_result=val_result["name"]

            read_device_list={"IP":ip_result, "Mac":mac_result,"Manufaturer":man_result,"Category":cat_result}
            
            show_dataframe_devices.append(read_device_list)

    device_df=pd.DataFrame(show_dataframe_devices)
    segmented_network=lit.data_editor(device_df,column_config={'Category':lit.column_config.SelectboxColumn('Category', width='medium',options=[ 
                            "Home",
                            "Personal",
                            "Work",
                            "Network Device",])},width=5500, height=600)
    
    if save_devices:
        show_dataframe_devices.clear()
        lit.write("Your Device list has been updated")
        #database.child(user['localId']).child('vault').child(device_item.key()).update(save_edit_device_data)
                                   
          
saved_device_list=[]
new_list_devices_nmap=[]
full_list_devices_nmap=[]

def devices_scan():

    auth=Firebase.firebaseconfig.firebase_auth()    
    database=Firebase.firebaseconfig.firebase_database()
    
    user=auth.sign_in_with_email_and_password('test1@gmail.com','D4nc3r$')

    tab1,tab2,tab3=lit.tabs(['Saved Devices','Scan Network','Network Segmentation'])


    with tab1:
        lit.write("This is your device : ", thisdevice())
        
        # UX / UI creating columns to return results into rows with headers    
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
                mac_s.write(s_result["mac"])
                manuf_s.write(s_result["manufacturer"])
                category_s.write(s_result["name"])

                #putting SAVED DEVICES into a list to call later for reference
                current_devices={"ip":s_result["ip"],"mac":s_result["mac"],"manufacturer":s_result["manufacturer"],"name":s_result["name"]}
                saved_device_list.append(current_devices)

        except:
            lit.warning("No devices saved to your database")
    
## ______________________________________________________________________________________________________________________##

    # TAB for all Scanning
    with tab2:
        one,two,three=lit.columns(3)
        full_scan=one.button("Full Scan Saved and New")
        scan=three.button("Scan for new devices")
        
        # UI/UX Columns and Headers
        ip_sc,mac_sc,manuf_sc,category_sc =lit.columns(4)
        ip_sc.markdown("**IP Address**")
        mac_sc.markdown("**MAC Address**")
        manuf_sc.markdown("**Manufacturer**")
        category_sc.markdown("**Category**")

        
        # -- Running full scan and calling all devices on the network
        if full_scan:
            
        #if scan2=='Full Scan':
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


            # Writing to the database only if the device does not exist 
            for db_device in saved_device_list:
                device1=db_device['mac']  
                for scan_device in full_list_devices_nmap:
                    device2=scan_device['mac']
                    if device1!=device2:
                        database.child(user['localId']).child('Devices').push(scan_device)      

            
        # -- Running scan for only new devices not alrady in the database
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
                 

    with tab3:
        segment()          
