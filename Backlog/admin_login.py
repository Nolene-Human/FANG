#Initiate SDK Auth using OAuth2.0 google refresh token


        #AUTHENTICATION

#admin
#import database and authentication firebase_admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore 


import streamlit as lit
from streamlit_extras.switch_page_button import switch_page
import os

def admin_login():

    cred = r'C:\Users\Nina\Desktop\key\family-area-network-firebase-adminsdk-okm5h-984dd4e918.json'
    login=credentials.Certificate(cred)
    #firebase_admin.initialize_app(login)

#https://www.youtube.com/watch?v=_bElevccXl8


    #using os path to read if key is in sepecified location or not.
    os.path.exists(cred)
        #if no key is in specified location, show 'user login page'
    if os.path.exists(cred) == False:
           lit.write("Our system could not verify your system as an FAN System Administrator, did you meant to login as a FAN")
           Im_a_fan=lit.button("Yes, Log me in as a FAN User")
           register=lit.button("No, but would like to register")

           if Im_a_fan:
                   switch_page("a_fan_login")
           if register:
                   switch_page("Fan")
                   
    else:
        #FAN_admin = firebase_admin.initialize_app(cred)
        lit.write("Hi Admin")
        lit.write("Here is a list of all your users")

        db=firestore.client()

        fan_users=db.collection("user").stream()

        for users in fan_users:
              lit.write("{}".format(users.to_dict()))