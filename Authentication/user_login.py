
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

import launch_pages # Import applications Launch page function
import registered_pages.ZeroTrustFunctions

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
          database = Firebase.firebaseconfig.firebase_database()
    
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
               lit.subheader("Password Management Tool")
               tab1, tab2 = lit.tabs(["|  Vault Entry ","|  Your Vault "])
                         
               with tab1:
                                             
                    with lit.form("Enter Account Details",clear_on_submit=True):
                              
                         account_name=lit.text_input("Enter Account Name: ")
                         account_web=lit.text_input("Enter link to account")
                         account_username=lit.text_input("Enter Username: ")
                         password_entered = lit.text_input("Enter Password: ")

                         save_to_vault=lit.form_submit_button("Save Entry")

                    if account_web == None or account_username == None or account_name == None:
                         lit.sidebar.warning("This form needs all the data")

                         if save_to_vault:
                             #if  :
                                   #lit.warning("mmm, looks like we are missing some info here, please enter all data")
                                   
                                   # or password_entered == None:
                                   #      lit.sidebar.warning("mmm, looks like we are missing some info here, please enter all data")
                                   # elif account_web == None or account_username == None :
                                   #      lit.sidebar.warning("mmm, looks like we are missing some info here, please enter all data")
                                   
                                   #                               try:
                              data={"vault_account" : account_name,"vault_web":account_web,"vault_username" :account_name,"Account username":account_username,"vault_password":password_entered}
                              database.child(user['localId']).child("vault").push(data)
                              lit.success("Data saved to your vault")
                    

                    

               with tab2:
                    import pandas as pd
                    
                    vault_acc=database.child(user['localId']).child('vault').get()
                    for vault_item in vault_acc.each():
                         column_vault=(vault_item.val())
                         #lit.write(pd.json_normalize(column_vault))
                         update_vault=lit.experimental_data_editor(column_vault)
                         if update_vault:
                               database.child(user['localId']).child("vault").update(update_vault)
               
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
               import nmap
                   #https://blog.streamlit.io/editable-dataframes-are-here/
            #https://medium.com/codefile/customizing-streamlit-columns-4bfd58fcb7c9
       
               with lit.expander("Block Device"):
                    lit.write("How to remove a device from your network")
               
               scan = lit.checkbox("Scan for the list of devices conntect to the Newtork")
        
               nm = nmap.PortScanner()
               if scan:
                    lit.write("List of Devices on your network")
                    nm.scan(hosts='192.168.1.0/24', arguments='-sn')
                    
                    for host in nm.all_hosts():
                         if 'mac' in nm[host]['addresses']:
                              mac_address = nm[host]["addresses"]["mac"]
                              manufacturer = nm[host]["vendor"].get(mac_address, "Unknown")
                              lit.write("IP Address: {}, MAC Address: {}, Manufacturer: {}".format(host, mac_address, manufacturer))


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
        

          