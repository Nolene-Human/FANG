import streamlit as lit



#authentication
import pyrebase
import Firebase.firebaseconfig
import launch_pages.launch
import requests
import sys
import json


def register():

    # finding error code to call specific error messages for the user 
    error_url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyDwdy5R6ovvWadA_tV74J9-eEUN4Ghy3ME'
    r = requests.get(error_url)
    errorcode=r.status_code
    
    # cancel print of python call back errors on user screen
    sys.tracebacklimit=0

    launch_pages.launch.launch()

    firebase=Firebase.firebaseconfig.firebase_config()
    database=firebase.database()
    auth = firebase.auth()
    



    lit.sidebar.subheader("Lets get Registered")
     
    email=lit.sidebar.text_input("Your Email address")
    password=lit.sidebar.text_input("Enter your password",type="password")
    confirmpass=lit.sidebar.text_input("Confirm password",type="password")
    handle=lit.sidebar.text_input("Name : ",key="")

    submitted =lit.sidebar.checkbox("Register")

 
    if submitted:
        
        if password !=confirmpass:
            lit.sidebar.warning("Your passwords did not match please try again") 
                
        elif len(password) < 6:
            lit.sidebar.warning("Your password does not meet the minimum lenght of 6 characters")
        
        elif len(email)==0 or len(handle)==0:
            lit.sidebar.warning("mmm, looks like we are missing some info here, please enter all data")

        else:
            try:
                user=auth.create_user_with_email_and_password(email,password)
                lit.sidebar.success("Your Account has been created")
                database.child(user['localId']).child("ID").set(user['localId']) 
                database.child(user['localId']).child("AccountName").set(handle)
                database.child(user['localId']).child("Email").set(email)
                lit.sidebar.write("You can now login to your account to get started.")
            except:
                lit.sidebar.error("Email already exist!")


      