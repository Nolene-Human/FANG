
import streamlit as lit

import dashboard
import networksegmentation

# more streamlit imports



from streamlit_extras.switch_page_button import switch_page



from PIL import Image
import random

import Cyberhygiene.attacks
import pandas as pd
from requests import request

import json


import streamlit.components.v1 as components


# importing scanning function


import os

import passwordvault

lit.set_page_config(page_title="Your Space",page_icon='🚀', layout="wide")

logo=Image.open("Art/Pictures/banner.png")
lit.image(logo,caption="It's all for show productions")
lit.sidebar.write("Hi Nolene, Welcome to your space")

logout=lit.sidebar.button("logout")
if logout:
        switch_page("logout")

lit.header("""\n\n
        WELCOME TO THE FIRST step in reducing your home network's vulnerabilities against cyber attacks
\n""".upper())
lit.markdown("---")

tab1, tab2, tab3, tab4, tab5= lit.tabs(["|  dashboard ","|  password management tool ","|  cybersecurity plan/incident response plan ","|  devices on network ","|  network segmentation "])
with tab1:

        # -- get the devices mac address and print for user using uuid
        dashboard.dashboard()

<<<<<<< Updated upstream
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
=======
>>>>>>> Stashed changes

with tab2:   
        lit.subheader("Password Management Tool")
        col1, col2, col3= lit.columns(3)
        
        col1.write("Enter New Account")
        account_name=col1.text_input("Enter Account Name: ")
        account_username=col1.text_input("Enter Username: ")
        password_entered = col1.text_input("Password: ",type="password")
        save_password=col1.button("Save Entry")
        
        col2.write("List of Accounts")
        if save_password:
                col2.write(account_name)
                col2.write(account_username)
                show_pass=col2.button("Show Password")
                if show_pass:
                        col2.write(password_entered)
        
        
        gen_password=col3.button("or Generate a Strong Password")
        if gen_password:
               #Password Generator 
                letters = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
                ]
                numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

                nr_letters = 5
                nr_symbols = 5
                nr_numbers = 5

                password = []

                while nr_letters > 0:
                        pass_lett = random.choice(letters)
                        password.append(pass_lett)
                        nr_letters -= 1

                while nr_numbers > 0:
                        pass_num = random.choice(numbers)
                        password.append(pass_num)
                        nr_numbers -= 1

                while nr_symbols > 0:
                        pass_sym = random.choice(symbols)
                        password.append(pass_sym)
                        nr_symbols -= 1


                random.shuffle(password)
                col3.write("".join(password)) 


        



        generate_password=lit.button("Generate Password")
        if generate_password:
                passwordvault.generate_password()

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
                with lit.expander("Why you want to keep smart devices on a separate network"):
                        lit.write("More details here")

        with tab3:
                with lit.expander("Best Practice for Personal Devices"):
                        lit.write("More details here")
             
        with tab4:
                with lit.expander("Best Practice for Work devices in a Home Network"):
                        lit.write("More details here")

