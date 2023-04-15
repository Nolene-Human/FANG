

import streamlit as lit
import Firebase.firebaseconfig
import requests



#authentication
firebase=Firebase.firebaseconfig.firebase_config()
auth = firebase.auth()
database=firebase.database()

#calling functions
import registered_pages.dashboard
import launch_pages.launch


def user_login():
    
        email = lit.sidebar.text_input("Please enter your registered email")
        password = lit.sidebar.text_input("Please enter your password",type='password')

        login=lit.sidebar.checkbox("Submit")
                 
        if login:
            auth.sign_in_with_email_and_password(email,password)             
            registered_pages.dashboard.dashboard()
 
        else:
            launch_pages.launch.launch()
        

     

    