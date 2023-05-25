
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
    # returning error codes 
    error_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyDwdy5R6ovvWadA_tV74J9-eEUN4Ghy3ME'
    
    # cancel print of python call back errors on user screen
    sys.tracebacklimit=0
    
    

    #launch_pages.launch.launch() # keeps user on app launch page if not verified registered user

    # Calling all Firebase Database and Authentication functions from Firebase
    firebase = Firebase.firebaseconfig.firebase_config()   
    auth=Firebase.firebaseconfig.firebase_auth()
    database=Firebase.firebaseconfig.firebase_database()

    form,space,messages = lit.columns([6,1,6])

    ## UI/UX info on sidebar
  
    messages.error("SECURITY TIPS")
    messages.markdown("----")
    messages.write("[See if your account has already been compromised](https://haveibeenpwned.com/)")
    messages.markdown("----")
    messages.info("See our Cybersecurity Tips page for:")
    messages.markdown("- How to Maintain good password hygiene")
    messages.markdown("- What is Mutli Factor Authentications")
    messages.markdown("----")

    # Registration Form
    
   
    
    with form.form("Lets get Registered"):        

        lit.subheader("Lets get Registered")
            
            # User input
        email=lit.text_input("Your Email address")
        password=lit.text_input(":pushpin: We encourage STRONG PASSWORDS",type="password",help="As a minimum this password would need, At least 6 characters, Should contain a $ @ # ! symbol, and have at least one Uppercase")
        confirmpass=lit.text_input("Confirm password",type="password")
        handle=lit.text_input("Your Network Name : ")
        register_btn =lit.form_submit_button("Register")
        
            
            # Rules and Checks once user press the 'register' button 
        if register_btn:
                if password !=confirmpass:
                    lit.sidebar.warning("Your passwords do not match")
                    lit.stop()
                if email == "" or handle == "" or password==""or confirmpass=="":
                    lit.sidebar.warning("Please enter all fields")
                    lit.stop()
                
                try:
                        key=pyotp.random_base32()
                        if (Authentication.password_check.password_check(password)):

                            user=auth.create_user_with_email_and_password(email,password) # User is registered and authenticated through firebase.
                            
                            # Data entered creates user database account through set() 
                            database.child(user['localId']).child("AccountName").set(handle)
                            database.child(user['localId']).child("Email").set(email)
                            database.child(user['localId']).child("Userkey").set(key)
                            database.child(user['localId']).child("mfa").set(0)
                            database.child(user['localId']).child("vault").push({"accName" : handle,"web":"www.fang.com","username":email,"password":password})
                            # Sidebar gets updated with Success message
                            lit.sidebar.success("""Your Account has been created!\n
                            Next step, register for one time passcode authentication """)
                            lit.balloons()                       

            
                except requests.exceptions.HTTPError as error:
                    lit.sidebar.error("Please check check your email entered, it is either already registered or not a valid email.")

        
    
             

        
 
            
            
            


    
                 
