## ----------------------------------------THIS IS 'LOGIN FUNCTION' ------------------------------------------------------##
 ## -------------------------------- Called form fang.py when user select login---------------------------------------------##
## -------------------------- Uses Firebase_Config Functions to verify and log in users -----------------------------------##

### FUTURE DEVELOPMENT ###
# - Tick box in this area is not ideal
# - Form does not reset or hides when user logs in

## ______________________________________________________________________________________________________________________##

# Streamlit
import streamlit as lit

## ______________________________________________________________________________________________________________________##

#import launch_pages # Import applications Launch page function
import registered_pages.ZeroTrustFunctions.passwordvault

## ______________________________________________________________________________________________________________________##

import Firebase.firebaseconfig # Firebase Configuartion and Authentication Function
import registered_pages.zero_trust # if successfull navigate user to the zero_trust landing page -> User Dashboard


## ______________________________________________________________________________________________________________________##
def login(email,password):


     # Calling Firebase Config Authentication Function
     auth= Firebase.firebaseconfig.firebase_auth()

     user=auth.sign_in_with_email_and_password(email,password) # Authenticates registered users agains password
     database=Firebase.firebaseconfig.firebase_database()

     #read user data from database and write a greeting  message
     name=database.child(user['localId']).child('AccountName').get().val()
     lit.sidebar.subheader("Hi " + name + " Network")
     #return user


## ||________________________________________________End of Login______________________________________________________________________||##

## ||______________________________________________Start the User Page_________________________________________________________________||##



     # TABS accross the page to navigate to the various functions
     dashboard, vault, plan, devices, network, account = lit.tabs(["|  dashboard ","|  password vault ","|  cybersecurity plan/incident response plan ","|  devices on network ","|  network segmentation ","|  My Account "] )




     ## ______________________________________________________________________________________________________________________##
     with dashboard:
               # Shows the following details
               import uuid
               import socket
               #import Scanners.findhostdetails
     ## |______________________________________________________________________________________________________________________|##
               currentmachine, col2, col3,col4,col5, col6, col7,col8 = lit.columns([3,1,3,1,3,1,3,1])

               currentmachine.subheader("Machine details")

                         # -- get the devices mac address and print for user using uuid
               currentmachine.write("Details of this machine is : ")
               mac_addr = (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
               for elements in range(0,2*6,2)][::-1]))
               currentmachine.write("Mac Address : "+ mac_addr)
                         # -- get the devices mac address and print for user using socket
               try:
                    hostname = socket.gethostname()
                    currentmachine.write("Your Computer Name is : " + hostname)
               except:
                    currentmachine.write("Unable to get Hostname and IP")
               currentmachine.write("Your device ip address is : "+ registered_pages.findhostdetails.ip_address_lit())

          ## |______________________________________________________________________________________________________________________|##

               col3.subheader("Total Devices")
               col3.write("Total devices with last login: 14")
               col3.write("Total devices with this login: 16")

          ## |______________________________________________________________________________________________________________________|##

               col5.subheader("Network Activity")
               col5.write("Here is all the activities on your network in the last 24hours")

         ## |______________________________________________________________________________________________________________________|##

               with col7:
                    lit.subheader("Your cybersecurity checklist")

                    from streamlit_extras.stodo import to_do

                    scantodo=to_do(
                    [(lit.write, " Do a Network Scan")],
                    "scan",
                    )
                    passwordtodo=to_do(
                    [(lit.write, "Save your passwords")],
                    "password",
                    )
                    suspicioustodo=to_do(
                    [(lit.write, "Any suspicious activity on the network ")],
                    "suspicious"
                    )

     with vault:

          passentcol, passvaultcol = lit.columns(2)

          # Password Generator
          with passentcol:
               lit.subheader("Password Management Tool")
               button_generatePassword,password_generatePassword = lit.columns(2)
               with button_generatePassword:
                     generate_password=lit.checkbox("Give me a Strong Password")
               with password_generatePassword:
                     if generate_password:
                         lit.write(registered_pages.ZeroTrustFunctions.passwordvault.generate_password())

          ## |______________________________________________________________________________________________________________________|##

          # A FORM CREATE data to the password vault

               with lit.form("Enter Account Details into Vault",clear_on_submit=True):

                         account_name=lit.text_input("Enter Account Name: ")
                         account_web=lit.text_input("Enter link to account")
                         account_username=lit.text_input("Enter Username: ")
                         password_entered = lit.text_input("Enter Password: ",type='password')
                         save_to_vault=lit.form_submit_button("Save to Vault")

          # Conditions when button is pressed
               if save_to_vault:
                    data={"accName" : account_name,"web":account_web,"username":account_username,"password":password_entered}

                    if account_web == "" and account_username=="" and account_name=="" and password_entered=="":
                         lit.error("This form needs all the data")

          # Write data to database
                    else:
                         database.child(user['localId']).child("vault").push(data)
                         lit.success("Data saved to your vault")

               ## |______________________________________________________________________________________________________________________|##


          with passvaultcol:
               lit.subheader("This is your vault")

               # col1,col2,col3,col4=lit.columns(4)
               
               # col1.write("Username")
               # col2.write("Name")
               # col3.write("Password")
               # col4.write("Web Link")

               get_vault=database.child(user['localId']).child('vault').get()

               show_dataframe_vault=[]

               for vault in get_vault.each():
                    val_result=vault.val()

                    username_result=val_result["accName"]
                    usern_result=val_result["username"]
                    password_result=val_result["password"]
                    web_result=val_result["web"]

               # # # #      #     col1.write(account_username)
               # # # #      #     col2.write(vault_name)
               # # # #      #     col3.write(vault_password,type='password')
               # # # #      #     col4.write(vault_web)

                    read_vault_list={"Username":username_result, "Vault Name":usern_result,"Vault Password":password_result,"Web Link":web_result}
                    show_dataframe_vault.append(read_vault_list)

               lit.experimental_data_editor(show_dataframe_vault, use_container_width=True)



          ## |______________________________________________________________________________________________________________________|##
     with plan:

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

                        # should be a download button https://docs.streamlit.io/library/api-reference/widgets/lit.download_button
               lit.button("Export to PDF")

          ## |______________________________________________________________________________________________________________________|##

     with devices:

               # UX / UI creating tabs and columns to return results
               scan_for_devices_tab, view_update_devices_tab=lit.tabs(["Scan for new devices","View and Update Saved Devices"])

               with scan_for_devices_tab:
                    cola, colb = lit.columns([3,3])
                    with cola:
                         nmap=lit.checkbox("Show list of devices on your network")
                    with colb:
                         save_devices_nmap=lit.checkbox("Save / Update list to database")


                    ip_col,mac_col,manuf_col,name_col,succ_col=lit.columns([3,3,3,3,3])

                         # Column Headers
                    with ip_col:
                         lit.markdown("**IP Address**")
                    with mac_col:
                         lit.markdown("**MAC Address**")
                    with manuf_col:
                         lit.markdown("**Manufacturer**")
                    with name_col:
                         lit.markdown("**Device Name**")

                         # UX/UI for scanning Network
                    if nmap:
                         import nmap

                         nm = nmap.PortScanner()
                         nm.scan(hosts='192.168.1.0/24', arguments='-sn')
                         list_devices_nmap=[]


                         for host in nm.all_hosts():
                              if 'mac' in nm[host]['addresses']:
                                   mac_address = nm[host]["addresses"]["mac"]
                                   manufacturer = nm[host]["vendor"].get(mac_address, "Unknown")
                                   device_name=""
                                   with ip_col:
                                        lit.write(host)
                                   with mac_col:
                                        lit.write(mac_address)
                                   with manuf_col:
                                        lit.write(manufacturer)
                                   with name_col:
                                        lit.write("New\n")

                                   devices_nmap={"ip":host,"mac":mac_address,"manufacturer":manufacturer,"name":device_name}
                                   list_devices_nmap.append(devices_nmap)

                                   if save_devices_nmap:
                                        try:
                                             database.child(user['localId']).child('Devices').push(devices_nmap)
                                        except:
                                             lit.warning("No data")

               with view_update_devices_tab:
               # Read data into a dataframe

                    lit.write("Your saved Devices")
                    lit.write("To delete a device from your database")
                    update_devices=lit.checkbox("Update Changes")

                    show_dataframe_devices=[]
                    try:
                         get_your_devices=database.child(user['localId']).child('Devices').get()
                         
                         for device in get_your_devices.each():

                              result=device.val()
                              ip_result=result["ip"]
                              mac_result=result["mac"]
                              manuf_result=result["manufacturer"]
                              name_result=result["name"]
                              read_device_list={"IP Address":ip_result,"Mac Address":mac_result,"Manufacturer":manuf_result,"Name":name_result}
                              show_dataframe_devices.append(read_device_list)

                         lit.experimental_data_editor(show_dataframe_devices,use_container_width=True,num_rows="dynamic")



                    except:
                         lit.warning("No data yet")

                    if update_devices:
                         database
                         lit.write(show_dataframe_devices)
                    # for device_upd in show_dataframe_devices.each():

                    #       nameonly=device_upd.val()
                    #       update_name=nameonly["Name"]

                    #       database.child(user['localID']).child('Devices').update(update_name)

     with network:
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

     with account:
               lit.write("My Account")
               logout_user=lit.button("Logout")
               if logout_user:
                    lit.write("You are logged  out")

