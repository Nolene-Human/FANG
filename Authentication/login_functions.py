

import streamlit as lit
import Firebase.firebaseconfig
import requests

#authentication
firebase=Firebase.firebaseconfig.firebase_config()
auth = firebase.auth()


#calling functions
import registered_pages.dashboard
import launch_pages.launch


def user_login():
    
    
    email = lit.sidebar.text_input("Please enter your registered email")
    password = lit.sidebar.text_input("Please enter your password",type='password')

    login=lit.sidebar.button("login")
            
    if login:
        try:
            auth.sign_in_with_email_and_password(email,password)
            registered_pages.dashboard.dashboard()
        except requests.exceptions.RequestException as e:  
            lit.write( e)
    
    else:
        launch_pages.launch.launch()
        

    