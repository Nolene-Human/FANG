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

    firebaseConfig = {
        'apiKey': "AIzaSyDwdy5R6ovvWadA_tV74J9-eEUN4Ghy3ME",
        'authDomain': "family-area-network.firebaseapp.com",
        'databaseURL': "https://family-area-network-default-rtdb.asia-southeast1.firebasedatabase.app",
        'projectId': "family-area-network",
        'storageBucket': "family-area-network.appspot.com",
        'messagingSenderId': "601603660956",
        'appId': "1:601603660956:web:844e256757af50cc2be159",
        'measurementId': "G-JTL2XV1WG8"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)   
    auth=firebase.auth()
    database=firebase.database()
    



    lit.sidebar.subheader("Lets get Registered")
     
    email=lit.sidebar.text_input("Your Email address")
    password=lit.sidebar.text_input("Enter your password",type="password")
    confirmpass=lit.sidebar.text_input("Confirm password",type="password")
    handle=lit.sidebar.text_input("Name : ",key="")

    submitted =lit.sidebar.checkbox("Register")
    passwordlen = len(password)
 
    if submitted:
        
        user=auth.create_user_with_email_and_password(email,password)
        #user=auth.sign_in_with_email_and_password(email,password)
        database.child(user['localId']).child("AccountName").set(handle)
        database.child(user['localId']).child("Email").set(email)
        lit.sidebar.success("Your Account has been created")
        lit.sidebar.write("You can now login to your account to get started.")
            
        #except:
            #lit.sidebar.error(errorcode)
        
        if password !=confirmpass:
            lit.sidebar.warning("Your passwords did not match please try again") 
                
        elif passwordlen < 6:
            lit.sidebar.warning("Your password does not meet the minimum lenght of 6 characters")
        
        elif email == None or handle == None:
            lit.sidebar.warning("mmm, looks like we are missing some info here, please enter all data")


      