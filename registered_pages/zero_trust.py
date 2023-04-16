import streamlit as lit
from PIL import Image


import registered_pages.findhostdetails
import registered_pages.ZeroTrustFunctions.scannetworkdevices
import registered_pages.ZeroTrustFunctions.passwordvault

# importing scanning function
import uuid
import socket


def dashboard():
  
        lit.sidebar.button("logout")

        ## --------------------------- Initiate TABS accross Page ----------------------------------------------------- ##

        tab1, tab2, tab3, tab4, tab5, tab6 = lit.tabs(["|  dashboard ","|  password management tool ","|  cybersecurity plan/incident response plan ","|  devices on network ","|  network segmentation ","|  My Account "] )
        
        ## --------------------------------------------------------------------------------------------------------------#

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
                registered_pages.ZeroTrustFunctions.passwordvault.add_password()


        # --------------------------------------------------------------------------------------#

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
            
            # should be a download button https://docs.streamlit.io/library/api-reference/widgets/st.download_button
            lit.button("Export to PDF")

        # ---------------------------------------------------------------------------------------# 

        with tab4:
                registered_pages.ZeroTrustFunctions.scannetworkdevices.scan_network_devices()
        
        # ---------------------------------------------------------------------------------------#
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

        with tab6:
               lit.header("Your account info")
               
        
            