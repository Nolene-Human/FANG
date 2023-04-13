import streamlit as lit
from PIL import Image
# more streamlit imports
from streamlit_extras.switch_page_button import switch_page
import registered_pages.findhostdetails

from streamlit_extras.mention import mention

import streamlit.components.v1 as components


# importing scanning function
import uuid
import socket

import os

import registered_pages.passwordvault


def test():
    lit.header("""\n\n
        Welcome Nolene 
\n""".upper())

    tab1, tab2, tab3, tab4, tab5,= lit.tabs(["|  dashboard ","|  password management tool ","|  cybersecurity plan/incident response plan ","|  devices on network ","|  network segmentation "])
    with tab1:
            col1, col2, col3 = lit.columns(3) 
            
            col1.subheader("Machine details")        
            
            # -- get the devices mac address and print for user using uuid
            col1.write("Details of this machine is : ")
            mac_addr = (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
            for elements in range(0,2*6,2)][::-1]))
            col1.write("Mac Address : " + mac_addr) 
            # -- get the devices mac address and print for user using socket
            try:
                hostname = socket.gethostname()
                col1.write("Your Computer Name is : " + hostname)
            except:
                col1.write("Unable to get Hostname and IP")
            col1.write("Your device ip address is : "+ registered_pages.findhostdetails.ip_address_lit())

            col2.subheader("Total Devices")
            col2.write("Total devices with last login: 14")
            col2.write("Total devices with this login: 16")
            

            col3.subheader("Network Activity")
            col3.write("Here is all the activities on your network in the last 24hours")
            

    with tab2:   
            lit.subheader("Password Management Tool")
            col1, col2, col3 = lit.columns(3,gap="large")
            
            col1.write("Enter New Account")
            account_name=col1.text_input("Enter Account Name: ")
            account_web=col1.text_input("Enter link to account")
            account_username=col1.text_input("Enter Username: ")
            password_entered = col1.text_input("Password: ",type="password")
            save_password=col1.button("Save Entry")
            
            col2.write("List of Accounts")
            if save_password:
                    col2.write("Account name: "+account_name)
                    col2.write("Username: "+account_username)
                    col2.write("Link: "+account_web)
                    show_pass=col2.button("Show Password")
                    if show_pass:
                            col2.write(password_entered)

            password=col3.button("Generate a strong password")
            if password:
                    registered_pages.passwordvault.generate_password()

    with tab3:   
            lit.write("cybersecurity plan/incident response plan")
            
            #Cyberhygiene.attacks.attacks_lit()
            #lit.button("Generate a Plan")
            
            lit.write("""THIS IS YOUR PLAN \n\n
            1. Goals & Plan to prevent cyber attacks.\n
                    - Limiting who accesses information.\n
                    - Restricting internet browsing on your network.\n
                    - Implementing a plan of action for suspicious emails.\n
            2. Potential threats.\n
            3. Security policies.\n
            4. A breach response plan.\n
            5. Communicating the incident. """)
            lit.button("Export to PDF")

    with tab4:
        #https://blog.streamlit.io/editable-dataframes-are-here/
            #https://medium.com/codefile/customizing-streamlit-columns-4bfd58fcb7c9
            import nmap   

            with lit.expander("Block Device"):
                    lit.write("How to remove a device from your network")
            scan = lit.button("Scan for list of devices conntect to the Newtork")
            nm = nmap.PortScanner()
            if scan:
                    lit.write("List of Devices on your network")
                    nm.scan(hosts='192.168.1.0/24', arguments='-sn')
                    
                    for host in nm.all_hosts():
                            if 'mac' in nm[host]['addresses']:
                                    mac_address = nm[host]["addresses"]["mac"]
                                    manufacturer = nm[host]["vendor"].get(mac_address, "Unknown")
                                    lit.write("IP Address: {}, MAC Address: {}, Manufacturer: {}".format(host, mac_address, manufacturer))
                                    



                    devices=lit.button("Save Changes")

    with tab5:
            import pandas as pd
            tab1, tab2, tab3, tab4  = lit.tabs(["SEGMENT YOUR NETWORK","LIST OF SMART DEVICES","LIST OF PERSONAL DEVICES","LIST OF WORK DEVICES"]) 
            
            with tab1:
                    #group=lit.selection(("Smart Device","Work Device","Private Device"))

                    df = pd.DataFrame(
                    [
                            {"Ip Address": "265.265.265.265", "Mac Address": "00:00:00:00:00", "Manufacturer":"Tibro","Group":" "},
                            {"Ip Address": "265.265.265.265", "Mac Address": "00:00:00:00:00", "Manufacturer":"Tp-link Technologies","Group":" "},
                            {"Ip Address": "265.265.265.265", "Mac Address": "00:00:00:00:00", "Manufacturer":" Philips Lighting BV","Group":" "},
                            {"Ip Address": "265.265.265.265", "Mac Address": "00:00:00:00:00", "Manufacturer":"Unknown","Group":" "},
                    ]
                    )

                    lit.dataframe(df, use_container_width=True)
            
            with tab2:
                    with lit.expander("Best Practice for Smart Devices"):
                            lit.write("More details here")

            with tab3:
                    with lit.expander("Best Practice for Personal Devices"):
                            lit.write("More details here")
                
            with tab4:
                    with lit.expander("Best Practice for Work devices in a Home Network"):
                            lit.write("More details here")