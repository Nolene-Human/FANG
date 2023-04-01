import streamlit as lit
# more streamlit imports
from streamlit_extras.switch_page_button import switch_page
import Scanners.findhostdetails



import streamlit.components.v1 as components


# importing scanning function
import uuid
import socket

import os

import passwordvault

lit.set_page_config(page_title="Your Space",page_icon='🚀', layout="wide")

lit.sidebar.write("Hi User, Welcome to your space")



lit.header("""\n\n
        WELCOME TO THE FIRST step in reducing your home network's vulnerabilities against cyber attacks
\n""".upper())
lit.markdown("---")

tab1, tab2, tab3, tab4, tab5,= lit.tabs(["|  your machine ","|  password management tool ","|  cybersecurity plan/incident response plan ","|  devices on network ","|  network segmentation "])
with tab1:
        
        # -- get the devices mac address and print for user using uuid

        lit.subheader("Details of this machine is : ")
        lit.write ("You will see this format throughout this tool.\n")


        mac_addr = (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
        for elements in range(0,2*6,2)][::-1]))

        lit.write("Mac Address : " + mac_addr) 

        # -- get the devices mac address and print for user using socket

        try:
            hostname = socket.gethostname()
            lit.markdown("Your Computer Name is : " + hostname)

        except:
            lit.write("Unable to get Hostname and IP")


        lit.write("Your device ip address is : "+ Scanners.findhostdetails.ip_address_lit())

with tab2:   
        lit.write("password management tool")

        generate_password=lit.button("Generate Password")
        if generate_password:
                passwordvault.generate_password()

with tab3:   
        lit.write("cybersecurity plan/incident response plan")

with tab4:
       lit.write("devices on network, tag your device")

with tab5:
        tab1, tab2, tab3 = lit.tabs(["LIST OF SMART DEVICES","LIST OF PERSONAL DEVICES","LIST OF WORK DEVICES"]) 
        with tab1:
                with lit.expander("Why you want to keep smart devices on a separate network"):
                        lit.write("More details here")

        with tab2:
                with lit.expander("Best Practice for Personal Devices"):
                        lit.write("More details here")
             
        with tab3:
                with lit.expander("Best Practice for Work devices in a Home Network"):
                        lit.write("More details here")

