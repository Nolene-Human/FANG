
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
          #registered_pages.zero_trust.dashboard() # Once Authenticated then the users dashboard with user details are displayed   
                    
          # Database Get function to display Welcome message in Sidebar
          database=Firebase.firebaseconfig.firebase_database()
          name=database.child(user['localId']).child('AccountName').get().val()
          lit.sidebar.markdown("---------------------------")
          lit.sidebar.subheader("Hi " + name)
          lit.sidebar.markdown("---------------------------")
          database = Firebase.firebaseconfig.firebase_database()
    

          lit.subheader("Password Management Tool")
          tab1, tab2 = lit.tabs(["|  Vault Entry ","|  Your Vault "])
                    
          with tab1:
               
               if "save_to_vault" not in lit.session_state:
                    lit.session_state.button_clicked=False
               
                            
               with lit.form("Enter Account Details"):
                    account_name=lit.text_input("Enter Account Name: ")
                    account_web=lit.text_input("Enter link to account")
                    account_username=lit.text_input("Enter Username: ")
                    password_entered = lit.text_input("Enter Password: ")

               
                    save_to_vault=lit.form_submit_button("Save Entry")
                    lit.session_state.button_clicked=True

                    if save_to_vault:
                         data={"vault_account" : account_name,"vault_web":account_web,"vault_username" :account_name,"Account username":account_username,"vault_password":password_entered}
                         database.child(user['localId']).child("vault").push(data)
                         lit.success("Data saved to your vault")
                         


          with tab2:
               
                    vault_acc=database.child(user['localId']).child('vault').get().val()
                    #lit.write(vault_acc)
                    vault_print=json.dumps(vault_acc)
                    vault_print=vault_print.replace('{',"")
                    vault_print=vault_print.replace('"',"")
                    vault_print=vault_print.replace('-',"")
                    vault_print=vault_print.replace('}',"")
                    for n in vault_print.split(','):
                         lit.write(n)
                         lit.write('')
                    
     else:
          launch_pages.launch.launch()
  
        

#       lit.error(" This looks phishy? Are you attempting a Dictionary Attack? Cause we limit your attempts to three tries, sheer brute force won't work.",icon="🤖")
#       lit.write("But users are human so if you forgot your password press reset to go through the authentication process")
        

          