## ----------------------------------------THIS IS 'LOGIN FUNCTION' ------------------------------------------------------##
 ## -------------------------------- Called form fang.py when user select login---------------------------------------------##
## -------------------------- Uses Firebase_Config Functions to verify and log in users -----------------------------------##

### FUTURE DEVELOPMENT ###
# - Tick box in this area is not ideal
# - Form does not reset or hides when user logs in

## ______________________________________________________________________________________________________________________##

# Streamlit
import streamlit as lit



import json

## ______________________________________________________________________________________________________________________##

#import launch_pages # Import applications Launch page function
import launch_pages.launch
import registered_pages.ZeroTrustFunctions.passwordvault

## ______________________________________________________________________________________________________________________##

import Firebase.firebaseconfig # Firebase Configuartion and Authentication Function
import registered_pages.zero_trust # if successfull navigate user to the zero_trust landing page -> User Dashboard


## ______________________________________________________________________________________________________________________##
def login():

     # Calling Firbase Config Authentication Function
     auth= Firebase.firebaseconfig.firebase_auth()
     
     email = lit.sidebar.text_input("Please enter your registered email")
     password = lit.sidebar.text_input("Please enter your password",type='password')
     
     login_btn=lit.sidebar.checkbox("Login")
     lit.sidebar.button("Reset Password")
     
          
          # Rules and Checks once user press the 'login' button              
     if login_btn:
               
          auth= Firebase.firebaseconfig.firebase_auth()
          user=auth.sign_in_with_email_and_password(email,password) # Authenticates registered users agains password
          # Once Authenticated then the users dashboard with user details are displayed   
                    
          # Database Get function to display Welcome message in Sidebar
          database=Firebase.firebaseconfig.firebase_database()
          name=database.child(user['localId']).child('AccountName').get().val()
          lit.sidebar.markdown("---------------------------")
          lit.sidebar.subheader("Hi " + name)
          lit.sidebar.markdown("---------------------------")
          lit.session_state=()
          logout_user=lit.sidebar.button("Logout")

          if logout_user:
                auth.revoke_refresh_tokens(user)


       
    
    ## ||________________________________________________End of Login______________________________________________________________________||##


    
          # Initiate TABS accross Page 
          dashboard, vault, plan, devices, network, account = lit.tabs(["|  dashboard ","|  password vault ","|  cybersecurity plan/incident response plan ","|  devices on network ","|  network segmentation ","|  My Account "] )
          

     ## ______________________________________________________________________________________________________________________##
          with dashboard:
               import uuid
               import socket
                    #import Scanners.findhostdetails
          ## |______________________________________________________________________________________________________________________|##
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
                
         ## |______________________________________________________________________________________________________________________|##       
          with vault:
          
          # Password Generator

               lit.subheader("Password Management Tool")
               button_generatePassword,password_generatePassword = lit.columns(2)
               with button_generatePassword:
                     generate_password=lit.checkbox("Give me a Strong Password")
               with password_generatePassword:
                     if generate_password:
                         lit.write(registered_pages.ZeroTrustFunctions.passwordvault.generate_password())
               

               tab1, tab2, expr_panda = lit.tabs(["|  Vault Entry ","|  Your Vault ", "Panda"])
          ## |______________________________________________________________________________________________________________________|##  
          
          # A FORM CREATE data to the password vault       
               with tab1:
                                             
                    with lit.form("Enter Account Details into Vault",clear_on_submit=True):
                              
                         account_name=lit.text_input("Enter Account Name: ")
                         account_web=lit.text_input("Enter link to account")
                         account_username=lit.text_input("Enter Username: ")
                         password_entered = lit.text_input("Enter Password: ")

                         save_to_vault=lit.form_submit_button("Save to Vault")

                         

          # Conditions when button is pressed 
                    if save_to_vault:  
                         
                         vault_acc_check=database.child(user['localId']).child('vault').get("vault_web")
                         data={"vault_account" : account_name,"vault_web":account_web,"account username":account_username,"vault_password":password_entered}
                         
                                                  
                         if account_web == "" and account_username=="" and account_name=="" and password_entered=="":
                              lit.error("This form needs all the data")

#### LEFT OFF HERE ################
                         for vault_check in vault_acc_check.each():
                               duplicate=vault_check.val()['vault_web']
                               if duplicate == account_web:
                                     lit.error("This web account link has already been entered")
                         
          # Write data to database
                         else:
                                   database.child(user['localId']).child("vault").push(data)
                                   lit.success("Data saved to your vault")
                    
               ## |______________________________________________________________________________________________________________________|##

          # READ / UPDATE / DELETE password vault data
               
               with tab2:
                    import pandas as pd

               # READ     
                    vault_acc=database.child(user['localId']).child('vault').get()


                    for vault_item in vault_acc.each():
                         
                         writevault,changevault=lit.columns([3,6])

               #UPDATE          
                         with changevault:
                              drop_vault=(vault_item.key(),'1')
                              edit,delete = lit.tabs(["Edit","Delete"])
                              with edit:
                                   vault_to_edit, confirm_vault_edit = lit.columns(2)
                                   with vault_to_edit:
                                        save_vault=(vault_item.key(),'2')
                                        #vault_panda=pd.DataFrame(vault_item)
                                        #lit.write(vault_panda)
                                        save_edit_vault_data=lit.experimental_data_editor(vault_item.val(), key=drop_vault)
                                   with confirm_vault_edit:
                                        save_vault_edit=lit.button("Save Changes",key=save_vault)
                                        if save_vault_edit:                                         
                                             database.child(user['localId']).child('vault').child(vault_item.key()).update(save_edit_vault_data)
               #DELETE            
                              with delete:
                                  
                                   delete_vault=(vault_item.key(),'3')
                                   lit.error("🚨 Sure you want to delete this account")
                                   vault_delete_option=lit.radio("  ",("No","Yes"),key=delete_vault)
                                   if vault_delete_option == 'Yes':
                                        database.child(user['localId']).child('vault').child(vault_item.key()).remove()
                                        lit.write("Account was deleted, it will refresh shortly")
                                   if vault_delete_option =="No":
                                        lit.success("Account not yet deleted, please confirm by selecting yes")
                    
                    # READ vault data on screen for the user                         
                         with writevault:
                             lit.write(vault_item.val())        

          # Test Code for better tables

               with expr_panda:
                    lit.write ("see code")

                    vault_acc=database.child(user['localId']).child('vault').get()
                    column_vault=(vault_item.val())
                    
                    vault_panda=pd.DataFrame(vault_acc.val())
                    lit.write(vault_panda)
                    title_column={"Account" : vault_panda}
                    lit.write (title_column)
                    lit.write("https://www.youtube.com/watch?v=zN2Hua6oII0")
                     
               
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
                        
                        # should be a download button https://docs.streamlit.io/library/api-reference/widgets/st.download_button
               lit.button("Export to PDF")

          ## |______________________________________________________________________________________________________________________|##  

          with devices:
               import scapy.all as s
           
               #Run the scan of the network
               run=lit.checkbox("Run a scan")
               list_devices = {}
               list_devices['Devices'] = []
               
               if run:
                         answered_list=s.arping("192.168.1.0/24")
               
                    # iterate through the result and add each host to the dictionary
                         for sent, received in answered_list[0].res:
                              list_devices['Devices'].append({
                                   'ip': received.psrc,
                                   'mac': received.hwsrc,
                                   'name': ""
                                   #'vendor': received.hwtype
                         })
               
               #lit.json(list_devices)

               #Compare to database and list new devices

               save_devices=lit.checkbox('Save Entries')
               # Write to database
               if save_devices:
                    ip=received.psrc
                    mac=received.hwsrc
                    name=""
                    your_devices={"ip":ip,"mac":mac,"name":name}
                    database.child(user['localId']).child('devices').push(your_devices)
                                
               
               # lit.write("Your saved Devices")
               # get_your_devices=database.child(user['localId']).child('devices').get()
               # col1,col2,col3=lit.columns([3,3,3])
                    
               # for device in get_your_devices.each():
               #      result=device.val()
               #      ip_result=result["ip"]
               #      mac_result=result["mac"]
               #      name_result=result["name"]

               #      with col1:     
               #           lit.write(ip_result) 
               #      with col2:
               #           lit.write(mac_result)

               #      with col3:
               #            lit.write(name_result)
                         

               


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

          
     else:
          launch_pages.launch.launch() 
  
        

#       lit.error(" This looks phishy? Are you attempting a Dictionary Attack? Cause we limit your attempts to three tries, sheer brute force won't work.",icon="🤖")
#       lit.write("But users are human so if you forgot your password press reset to go through the authentication process")