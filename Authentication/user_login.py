
## ----------------------------------------THIS IS 'LOGIN FUNCTION' ------------------------------------------------------##
 ## -------------------------------- Called form fang.py when user select login---------------------------------------------##
## -------------------------- Uses Firebase_Config Functions to verify and log in users -----------------------------------##

### FUTURE DEVELOPMENT ###
# - no future developmentsni
## ______________________________________________________________________________________________________________________##


import Firebase.firebaseconfig # Firebase SDK's

## ______________________________________________________________________________________________________________________##

import streamlit as lit


def login_form():
  database=Firebase.firebaseconfig.firebase_database()
  auth= Firebase.firebaseconfig.firebase_auth()

  with lit.form("User_Login"):        

        lit.subheader("Login")
            
        # User input
        email=lit.text_input("Your Email address")
        password=lit.text_input("Confirm password",type="password")
        login_button =lit.form_submit_button("Login")

        if email == "" or password=="":
                lit.warning("Please enter all fields")

        if login_button:
            try:
                user = auth.sign_in_with_email_and_password(email,password)
                name=database.child(user['localId']).child('AccountName').get().val()
                lit.success("Hi " + name +" You are logged in!")                        
                
            except:
                lit.error("Please enter the valid credentials")



def verify_user():
   lit.write("verify user")


def reset_password():
    with lit.form("Reset_Password"):        

        lit.subheader("Reset Password")
            
        # User input
        email=lit.text_input("Enter your email address")
        reset_button =lit.form_submit_button("Reset")

        if reset_button:
            lit.success("Instructions were sent to your email")
    