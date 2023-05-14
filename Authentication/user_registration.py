
   ## ----------------------------------------THIS IS 'REGISTRATION FUNCTION' ------------------------------------------------------##
 ## --------------------------- Called form Authentication/ user_registration.py when user select register ------------------------##
## -------------------------- Uses Firebase_Config functions to verify and register a new users -----------------------------------##

### FUTURE DEVELOPMENT ###
# - Built in tool to ensure strong password

## ______________________________________________________________________________________________________________________##

# Streamlit
import streamlit as lit

## ______________________________________________________________________________________________________________________##

import Firebase.firebaseconfig # Firebase Configuartion and Authentication function
import launch_pages.launch # Keep user on launch page while unauthorised or not logged in 
import Authentication.password_check

## ______________________________________________________________________________________________________________________##

import requests # used to get more details on excemption rule when needed
import sys # used to not print call back error on screen

## ______________________________________________________________________________________________________________________##
def register():

    # returning error codes 
    error_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyDwdy5R6ovvWadA_tV74J9-eEUN4Ghy3ME'
    
    # cancel print of python call back errors on user screen
    sys.tracebacklimit=0
    
    col1,col2=lit.columns(2)

    #launch_pages.launch.launch() # keeps user on app launch page if not verified registered user

    # Calling all Firebase Database and Authentication functions from Firebase
    firebase = Firebase.firebaseconfig.firebase_config()   
    auth=Firebase.firebaseconfig.firebase_auth()
    database=Firebase.firebaseconfig.firebase_database()

    ## UI/UX for Registration form on the sidebar
    
    with col1.form("Lets get Registered"):
   
        email=lit.text_input("Your Email address")
        password=lit.text_input("Enter your password",type="password")
        confirmpass=lit.text_input("Confirm password",type="password")
        handle=lit.text_input("Name : ")

        rego, cl_rego=lit.columns(2)
        with rego:
            register_btn =lit.form_submit_button("Register")
        with cl_rego:
            clear_rego = lit.form_submit_button ("Clear Form")
    
        # Rules and Checks once user press the 'register' button 
        if register_btn:

            try:
                if password !=confirmpass:
                    lit.sidebar.warning("Your passwords did not match please try again")
                    lit.stop() 
                if email == "" or handle == "" or password==""or confirmpass=="":
                    lit.sidebar.warning("mmm, looks like we are missing some info here, please enter all data")
                    lit.stop()
                if (Authentication.password_check.password_check(password)):
                    user=auth.create_user_with_email_and_password(email,password) # User is registered and authenticated through firebase.
                    auth.send_email_verification(user['idToken'])
                    # Data entered creates user database account through set() 
                    database.child(user['localId']).child("AccountName").set(handle)
                    database.child(user['localId']).child("Email").set(email)
                    database.child(user['localId']).child("vault").push({"vault_name" : handle,"vault_web":"www.fang.com","account_username":email,"vault_password":password})
                    
                    # Sidebar gets updated with Success message
                    lit.sidebar.success("""Your Account has been created and you can now login to get started
                    We have sent you a verification email, please check your junk folder.""")
                
            except requests.exceptions.HTTPError as error:
                       lit.sidebar.error("There was a problem please check your email entered.")

                
        col2.info("""
        We encourage having a STRONG PASSWORD\n 
        1. See our Cybersecurity Tips page for ideas  \n
        2. This password would need :\n
        a. At least 6 characters\n
        b. Should contain a $ @ # symbol\n
        c. At least one uppercase
        """)
        col2.error("[See if your account has already been compromised](https://haveibeenpwned.com/)")
        


