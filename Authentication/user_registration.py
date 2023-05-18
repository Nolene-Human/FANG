
   ## ----------------------------------------THIS IS 'REGISTRATION FUNCTION' ------------------------------------------------------##
 ## --------------------------- Called form Authentication/ user_registration.py when user select register ------------------------##
## -------------------------- Uses Firebase_Config functions to verify and register a new users -----------------------------------##

### FUTURE DEVELOPMENT ###
# - Built in tool to ensure strong password

## ______________________________________________________________________________________________________________________##

# Streamlit
import streamlit as lit
from PIL import Image #used to display images on page

## ______________________________________________________________________________________________________________________##

import Firebase.firebaseconfig # Firebase Configuartion and Authentication function
import launch_pages.launch # Keep user on launch page while unauthorised or not logged in 
import Authentication.password_check
import Authentication.mfa

import pyotp
import qrcode

## ______________________________________________________________________________________________________________________##

import requests # used to get more details on excemption rule when needed
import sys # used to not print call back error on screen

## ______________________________________________________________________________________________________________________##
def register():
    userkey=pyotp.random_base32()

    # returning error codes 
    error_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyDwdy5R6ovvWadA_tV74J9-eEUN4Ghy3ME'
    
    # cancel print of python call back errors on user screen
    sys.tracebacklimit=0
    
    

    #launch_pages.launch.launch() # keeps user on app launch page if not verified registered user

    # Calling all Firebase Database and Authentication functions from Firebase
    firebase = Firebase.firebaseconfig.firebase_config()   
    auth=Firebase.firebaseconfig.firebase_auth()
    database=Firebase.firebaseconfig.firebase_database()

    ## UI/UX for Registration form on the sidebar
    
    

    lit.sidebar.markdown("\n\n")

    lit.sidebar.error("SECURITY TIPS")

    lit.sidebar.markdown("----")

    lit.sidebar.write("[See if your account has already been compromised](https://haveibeenpwned.com/)")
    lit.sidebar.markdown("----")
    lit.sidebar.info("See our Cybersecurity Tips page for:")
    lit.sidebar.markdown("- How to Maintain good password hygiene")
    lit.sidebar.markdown("- What is Mutli Factor Authentications")
    lit.sidebar.markdown("----")

    col1,space,col2=lit.columns([5,1,5])

       

    col2.markdown("**You will need a Multi-Factor one-time-passcode to use this application**")
    col2.write("Scan the QRcode using your Google Authentication APP to get registered")
    
    
    col2.markdown("---")
    yourqr=pyotp.totp.TOTP(userkey).provisioning_uri(name="FANG",issuer_name="Family Area Network")
    qrcode.make(yourqr).save("yourqr.png")
    col2.image("yourqr.png",width=250)    

    col2.markdown("----")

    with col1.form("Lets get Registered"):
        lit.subheader("Lets get Registered")
        
   
        email=lit.text_input("Your Email address")
        password=lit.text_input(":pushpin: We encourage STRONG PASSWORDS",type="password",help="This password would need, At least 6 characters, Should contain a $ @ # symbol, and have at least one Uppercase")
        confirmpass=lit.text_input("Confirm password",type="password")
        handle=lit.text_input("Your Network Name : ")
        
        lit.markdown("---")

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
                    

                    # Data entered creates user database account through set() 
                    database.child(user['localId']).child("AccountName").set(handle)
                    database.child(user['localId']).child("Email").set(email)
                    database.child(user['localId']).child("Userkey").set(userkey)
                    database.child(user['localId']).child("vault").push({"accName" : handle,"web":"www.fang.com","username":email,"password":password})
                    

                    # Sidebar gets updated with Success message
                    col2.success("""Your Account has been created!.""")
                    lit.balloons()


            except requests.exceptions.HTTPError as error:
                       lit.sidebar.error("There was a problem please check your email entered.")
            

        
        
