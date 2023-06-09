
   ## ----------------------------------------THIS IS 'REGISTRATION FUNCTION' ------------------------------------------------------##
 ## --------------------------------- Called form fang.py when user select register ----------------------------------------------##
## -------------------------- Uses Firebase_Config functions to verify and register a new users -----------------------------------##

### FUTURE DEVELOPMENT ###
# - Tick box does not reset to false if user enters wrong details

## ______________________________________________________________________________________________________________________##

# Streamlit
import streamlit as lit

## ______________________________________________________________________________________________________________________##

import Firebase.firebaseconfig # Firebase Configuartion and Authentication Function
import launch_pages.launch # Keep user on launch page while unauthorised or logged in 

## ______________________________________________________________________________________________________________________##

import requests # used to get more details on excemption rule when needed
import sys # used to not print call back error on screen


## ______________________________________________________________________________________________________________________##
def register():

    # finding error code to call specific error messages for the user 
    error_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyDwdy5R6ovvWadA_tV74J9-eEUN4Ghy3ME'
    r = requests.get(error_url)
    errorcode=r.status_code
    
    # cancel print of python call back errors on user screen
    sys.tracebacklimit=0

    launch_pages.launch.launch()


    firebase = Firebase.firebaseconfig.firebase_config()   
    auth=firebase.auth()
    database=firebase.database()
    
    with lit.sidebar.form("Lets get Registered",clear_on_submit=True):
    # Side Bar update to Registration Form
         
        email=lit.text_input("Your Email address")
        password=lit.text_input("Enter your password",type="password")
        confirmpass=lit.text_input("Confirm password",type="password")
        handle=lit.text_input("Name : ")

        register_btn =lit.form_submit_button("Register")
    
        passwordlen = len(password)
    
        # Rules and Checks once user press the 'register' button 
        if register_btn:

            url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyDwdy5R6ovvWadA_tV74J9-eEUN4Ghy3ME'
            


            try:
                user=auth.create_user_with_email_and_password(email,password) # User is registered and authenticated through firebase.

                   # Data entered creates user database account through set() 
                database.child(user['localId']).child("AccountName").set(handle)
                database.child(user['localId']).child("Email").set(email)
                
                # Sidebar gets updated with Success message
                lit.sidebar.success("Your Account has been created")
                lit.sidebar.write("You can now login to your account to get started.")
                
                
            
             # Sidebar gets updated with error message if user does not pass the registration rules
            except:           
        
                if password !=confirmpass:
                    lit.sidebar.warning("Your passwords did not match please try again") 
                        
                if passwordlen < 6:
                    lit.sidebar.warning("Your password does not meet the minimum lenght of 6 characters")
                
                if email == "" or handle == "" or password==""or confirmpass=="":
                    lit.sidebar.warning("mmm, looks like we are missing some info here, please enter all data")
                
                if requests.HTTPError:
                    lit.sidebar.error("The email address entered is either incomplete or already registered")
                    lit.stop()
                        

                        

       




      