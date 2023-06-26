import streamlit as lit
import nmap   


import uuid
import socket
import subprocess
import pandas as pd


import Firebase.firebaseconfig
import Authentication.user_login_copy

database=Firebase.firebaseconfig.firebase_database()


loggedinUser=Authentication.user_login_copy.this_user_id



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
    for user in loggedinUser:
        id4=user['localID'] 
    
    edit_devices=database.child(id4).child('Devices').get()
    
    show_dataframe_devices=[]
    
    save_devices=lit.button("Save Categories")
    try:
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
    

        new_dict=segmented_network.to_dict('records')
        
        
    except:
        lit.write('No data in database')
        
    if save_devices:
        #show_dataframe_devices.clear()
        lit.write("Your Device list has been updated")
        database.child(id4).child('Devices').remove()
        for d in new_dict:
            current_devices={"ip":d["IP"],"mac":d["Mac"],"manufacturer":d["Manufaturer"],"name":d["Category"]}
            database.child(id4).child('Devices').push(current_devices)

                                   
          
saved_device_list=[]
new_list_devices_nmap=[]
full_list_devices_nmap=[]

def devices_scan():
    for user in loggedinUser:
        id5=user['localID'] 


    devices=lit.radio("Scan and Segment Network",('Saved Devices','Scan for new devices','Categorise Network Devices'),horizontal=True)
    
    if devices=='Saved Devices':

        lit.write("This is your device : ", thisdevice())
        
        # UX / UI creating columns to return results into rows with headers    
        ip_s,mac_s,manuf_s,category_s =lit.columns(4)
        ip_s.markdown("**IP Address**")
        mac_s.markdown("**MAC Address**")
        manuf_s.markdown("**Manufacturer**")
        category_s.markdown("**Category**")
        try:
            get_your_devices=database.child(id5).child('Devices').get()
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
    if devices=='Scan for new devices':
        
        one,two,three=lit.columns(3)
        full_scan=one.button("Full Scan Saved and New")
        #save_scan=two.checkbox("Save to database")

        # UI/UX Columns and Headers
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
                    

                
                #if save_scan:
                # Writing to the database only if the device does not exist 
                    if len(saved_device_list)==0:
                        database.child(id5).child('Devices').push(devices_nmap) 
                    else:
                        for scan_device in full_list_devices_nmap:
                            device2=scan_device['mac']
                            for db_device in saved_device_list:
                                device1=db_device['mac'] 
                                if device1!=device2:
                                    database.child(id5).child('Devices').push(devices_nmap)
                 

    if devices=='Categorise Network Devices':
        segment()          
