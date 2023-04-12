

import streamlit as lit
from streamlit_extras.switch_page_button import switch_page

#authentication
import pyrebase
import Firebase.firebaseconfig

#from Crypto.PublicKey import RSA

def user_login():
    
    Firebase.firebaseconfig.firebase_config()     
    #auth = firebase.auth()


    lit.header("Login to your network")

    email = lit.text_input("Please enter your username")
    password = lit.text_input("Please enter your password")

    user=[email,password]

    login=  lit.button("login")
    
    if login:
        lit.write("Welcome"+user[0])

    