import streamlit as lit
import nmap   

# 

def devices_scan():
    
    scan_for_devices_tab, view_update_devices_tab=lit.tabs(["Scan for new devices","View and Update Saved Devices"])
    
    with scan_for_devices_tab:
        lit.write("[Lookup the Mac address to see who is the manufacturer](https://mac.lc)")
        cola, colb = lit.columns([3,3])
        with cola:     
            nmap_scan=lit.checkbox("Show list of devices on your network")
        with colb:
            save_devices_nmap=lit.checkbox("Save / Update list to database")
    # UX / UI creating columns to return results into rows
        ip_col,mac_col,manuf_col,name_col,category_col=lit.columns(5)
    # Column Headers
        with ip_col:
            lit.markdown("**IP Address**")
        with mac_col:
            lit.markdown("**MAC Address**")
        with manuf_col:
            lit.markdown("**Manufacturer**")
        with name_col:
            lit.markdown("**Device Name**")
        with category_col:
            lit.markdown("**Provide Purpose**")                               
    # UX/UI for scanning Network 
        if nmap_scan: 
            new=nmap.PortScanner()         
            
            new.scan(hosts='192.168.1.0/24', arguments='-sn')
            list_devices_nmap=[] 

            for host in new.all_hosts():
                if 'mac' in new[host]['addresses']:
                    mac_address = new[host]["addresses"]["mac"]
                    manufacturer = new[host]["vendor"].get(mac_address, "Unknown")
                    device_name=""                                   
                    with ip_col:
                        lit.write(host)
                    with mac_col:
                        lit.write(mac_address)
                    with manuf_col:
                        lit.write(manufacturer)
                    with name_col:
                        lit.write("New\n")
                    with category_col:
                        lit.text_input("Purpose",label_visibility="collapsed",key=mac_address)

                    devices_nmap={"ip":host,"mac":mac_address,"manufacturer":manufacturer,"name":device_name}
                    list_devices_nmap.append(devices_nmap)

    return list_devices_nmap



# ,  column_config={
#         "Category": lit.column_config.SelectboxColumn(
#             "Device Category",
#             help="Where is the use main function ",
#             width="medium",
#             options=[
#                 "Home",
#                 "Personal",
#                 "Work",
#             ],
#         )
#     },
#     hide_index=True,)