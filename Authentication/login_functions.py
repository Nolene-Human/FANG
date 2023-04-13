

import streamlit as lit
from streamlit_extras.switch_page_button import switch_page

#authentication
import pyrebase
import Firebase.firebaseconfig
import registered_pages.test
import launch_pages.launch

#from Crypto.PublicKey import RSA

def user_login():
    
    
    

    Firebase.firebaseconfig.firebase_config()     
    #auth = firebase.auth()


    #lit.header("Login to your network")

    email = lit.sidebar.text_input("Please enter your username")
    password = lit.sidebar.text_input("Please enter your password",type='password')

    user=[email,password]

    login=  lit.sidebar.button("login")
    


    if login:
        registered_pages.test.test()

    else:
        launch_pages.launch.launch()