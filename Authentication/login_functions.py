

import streamlit as lit
from streamlit_extras.switch_page_button import switch_page

#authentication
import Authentication.user_registration
import pyrebase
from pyrebase import initialize_app
#from Crypto.PublicKey import RSA

def user_login():
    
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
    auth = firebase.auth()

    lit.header("Login to your network or Register to get started")

    email = lit.text_input("Please enter your username")
    password = lit.text_input("Please enter your password")

    user=[email,password]

    login=  lit.button("login")
    registration=lit.button("register")
    
    if login:
        lit.write("Welcome"+user[0])

    if registration:
          switch_page("registration")