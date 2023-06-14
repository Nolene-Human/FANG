import streamlit as lit
import nmap   

import Firebase.firebaseconfig



saved_mac_list=[]
list_devices_nmap=[]

def devices_scan():


    auth=Firebase.firebaseconfig.firebase_auth()    
    database=Firebase.firebaseconfig.firebase_database()
    
    user=auth.sign_in_with_email_and_password('test4@gmail.com','D4nc3r$')

    tab1,tab2=lit.tabs(['Saved Devices','Scan Network'])


    with tab1:
            
            scan=lit.button('Scan for new devices')
            # UX / UI creating columns to return results into rows
            ip_s,mac_s,manuf_s,category_s =lit.columns(4)
            # Column Headers                                
            # UX/UI for scanning Network 
            with ip_s:
                        lit.markdown("**IP Address**")
            with mac_s:
                        lit.markdown("**MAC Address**")
            with manuf_s:
                        lit.markdown("**Manufacturer**")
            with category_s:
                        lit.markdown("**Category**")

            try:
                get_your_devices=database.child(user['localId']).child('Devices').get()
                for saved in get_your_devices.each():
                    s_result=saved.val()
                    
                    with ip_s:
                        lit.write(s_result["ip"])
                    with mac_s:
                        saved_mac=lit.write(s_result["mac"])
                    with manuf_s:
                        lit.write(s_result["manufacturer"])
                    with category_s:
                        lit.write(s_result["name"])

                    saved_mac_list.append(saved_mac)
                   
            except:
                lit.write("No devices saved to your network")
            
            if scan:

                lit.write("[Lookup the Mac address to see who is the manufacturer](https://mac.lc)")
                new=nmap.PortScanner()         
            
                new.scan(hosts='192.168.1.0/24', arguments='-sn')
                 
                for host in new.all_hosts():
                
                    if 'mac' in new[host]['addresses']:
                        mac_address = new[host]["addresses"]["mac"]
                        manufacturer = new[host]["vendor"].get(mac_address, "Unknown")
                        device_name="New"

                        for saved in saved_mac_list:
                            call_mac=saved
                            if  call_mac!=mac_address:
                                with ip_s:
                                            lit.write(host)
                                with mac_s:
                                            lit.write(mac_address)
                                with manuf_s:
                                        lit.write(manufacturer)
                                with category_s:
                                        lit.write(device_name)
                                
                                devices_nmap={"ip":host,"mac":mac_address,"manufacturer":manufacturer,"name":device_name}
                                list_devices_nmap.append(devices_nmap)     
                                database.child(user['localId']).child('Devices').push(devices_nmap)        
            

    # with tab2:
    #     save_devices=lit.button('Save to Database')
 
    #             UX / UI creating columns to return results into rows
    #     ip_col,mac_col,manuf_col,category_col =lit.columns(4)
    #             Column Headers                                
    #             UX/UI for scanning Network 
    #     with ip_col:
    #         lit.markdown("**IP Address**")
    #     with mac_col:
    #         lit.markdown("**MAC Address**")
    #     with manuf_col:
    #         lit.markdown("**Manufacturer**")
    #     with category_col:
    #         lit.markdown("**Category**")

    #     lit.write("[Lookup the Mac address to see who is the manufacturer](https://mac.lc)")
    #     new=nmap.PortScanner()         
            
    #     new.scan(hosts='192.168.1.0/24', arguments='-sn')
    #     list_devices_nmap=[] 
    #     for host in new.all_hosts():
                
    #             if 'mac' in new[host]['addresses']:
    #                 mac_address = new[host]["addresses"]["mac"]
    #                 manufacturer = new[host]["vendor"].get(mac_address, "Unknown")
    #                 device_name="New"
    #                 for saved in saved_mac_list:
    #                     call_mac=saved
    #                     if  call_mac!=mac_address:
    #                         devices_nmap={"ip":host,"mac":mac_address,"manufacturer":manufacturer,"name":device_name}
    #                         list_devices_nmap.append(devices_nmap)
                            
                            
    # database.child(user['localId']).child('Devices').update(list_devices_nmap)

    # get_your_new_devices=database.child(user['localId']).child('Devices').get()


    # update_device=lit.data_editor(get_your_new_devices,  column_config={
    #                         "Name": lit.column_config.SelectboxColumn(
    #                         "Device Category",
    #                         help="Give this device its purpose in your network",
    #                         width="medium",
    #                         options=[
    #                         "Home",
    #                         "Personal",
    #                         "Work",
    #                         "Network Device",
    #                         ],)},
    #                         hide_index=True,)
    
    


                    # if save_devices_nmap:
                    #     try:
                    #         database.child(user['localId']).child('Devices').push(devices_nmap)
                    #         with view_update_devices_tab:

                    #             show_dataframe_devices=[]
                    #             get_your_devices=database.child(user['localId']).child('Devices').get()
                                                                    
                    #             for device in get_your_devices.each():
                                                                
                    #                 result=device.val()
                    #                 ip_result=result["ip"]
                    #                 mac_result=result["mac"]
                    #                 manuf_result=result["manufacturer"]
                    #                 name_result=result["name"]
                    #                 read_device_list={"IP Address":ip_result,"Mac Address":mac_result,"Manufacturer":manuf_result,"Name":name_result}
                    #                 show_dataframe_devices.append(read_device_list)

                    #             #update_list=
                    #             lit.data_editor(show_dataframe_devices,  column_config={
                    #                     "Name": lit.column_config.SelectboxColumn(
                    #                         "Device Category",
                    #                         help="Where is the use main function ",
                    #                         width="medium",
                    #                         options=[
                    #                             "Home",
                    #                             "Personal",
                    #                             "Work",
                    #                             "Network Device",
                    #                         ],
                    #                     )
                    #                 },
                    #                 hide_index=True,)
                          
            
            
        
    
            
                            
                        # except:
                        #         lit.warning("No data yet")

            #return list_devices_nmap