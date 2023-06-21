

   ## ----------------------------------------THIS IS 'REGISTRATION FUNCTION' ------------------------------------------------------##
 ## --------------------------- Called form Authentication/ user_registration.py when user select register ------------------------##
## -------------------------- Uses Firebase_Config functions to verify and register a new users -----------------------------------##

### FUTURE DEVELOPMENT ###
# - no future developments
## ______________________________________________________________________________________________________________________##

import streamlit as lit # Streamlit Front End

## ______________________________________________________________________________________________________________________##
import requests # used to get more details on excemption rule when needed
import sys # used to not print call back error on screen
## ______________________________________________________________________________________________________________________##

import Firebase.firebaseconfig # Firebase SDK's
import Authentication.password_check # password rules
import Authentication.mfa #otp functions

## ______________________________________________________________________________________________________________________##


def registration_form():
    # cancel print of python call back errors on user screen
    sys.tracebacklimit=0
        
    auth=Firebase.firebaseconfig.firebase_auth() #calling firebase authentication and assigning auth functions to variable auth
    database=Firebase.firebaseconfig.firebase_database() #calling firebase database and assigning database functions to variable database


    # UI/UX Registration Form
    with lit.form("Lets get Registered"):        

            lit.subheader("Lets get Registered")
                
            # User input
            email=lit.text_input("Your Email address")
            password=lit.text_input(":pushpin: We encourage STRONG PASSWORDS",type="password",help="As a minimum this password would need, At least 6 characters, Should contain a $ @ # ! symbol, and have at least one Uppercase")
            confirmpass=lit.text_input("Confirm password",type="password")
            handle=lit.text_input("Your Network Name : ")
            register_btn =lit.form_submit_button("Register")
            
            # Rules to check data has been entered correctly
            if password !=confirmpass:
                lit.warning("Your passwords do not match")
                #lit.stop()
            if email == "" or handle == "" or password==""or confirmpass=="":
                lit.warning("Please enter all fields")
                #lit.stop()              
                
            if register_btn:
              
                try:
                    if (Authentication.password_check.password_check(password)):
                        
                        user=auth.create_user_with_email_and_password(email,password) # User is registered and authenticated through firebase.
                            
                        # Data entered creates user database account through set() 
                        database.child(user['localId']).child("AccountName").set(handle)
                        database.child(user['localId']).child("Email").set(email)

                        #once user is successfully registered a unique key is generated and saved to their account
                        key=Authentication.mfa.key()
                        database.child(user['localId']).child("OTP").set(key)
                        database.child(user['localId']).child("mfa").set(0)
                        
                        # Success message
                        lit.success("Your Account has been created!")
                        lit.balloons()                       

                except requests.exceptions.HTTPError as error:
                    lit.error("Please check your email entered, it is either already registered or not a valid email.")

## ______________________________________________________________________________________________________________________##

def registration_messages():
    ## UI/UX info on sidebar
    lit.error("SECURITY TIPS")
    lit.markdown("----")
    lit.write("[See if your account has already been compromised](https://haveibeenpwned.com/)")
    lit.markdown("----")
    lit.info("See our Cybersecurity Tips page for:")
    lit.markdown("- How to Maintain good password hygiene")
    lit.markdown("- What is Mutli Factor Authentications")
    lit.markdown("----")
