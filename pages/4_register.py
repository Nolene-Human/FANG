import streamlit as lit
from PIL import Image
from streamlit_extras.switch_page_button import switch_page


#authentication
import pyrebase

import Firebase.firebaseconfig


lit.set_page_config(page_title="Register for a FANG Account ",page_icon='🚀', layout="wide")

logo=Image.open("Art/Pictures/banner.png")
lit.image(logo,caption="It's all for show productions")

fb_registration=Firebase.firebaseconfig.firebase_config()


auth = fb_registration.auth()
database=fb_registration.database()



lit.header("Let's get Registered")
FAN_name=lit.text_input("Give your Network a name: ",value="type here to give your network a unique name")
            
email=lit.text_input("Enter Your Email address")
password=lit.text_input("Enter your password: ",type="password")
confirmpass=lit.text_input("Confirm password: ",type="password")

submitted =lit.button("Register")
            
if submitted:
    if password!=confirmpass:
        lit.error(" Password does not match password confirmed", icon="🚨")
    else:
        user = auth.create_user_with_email_and_password(email,password)
        lit.success("Your Account has been created")
        user=auth.sign_in_with_email_and_password(email,password)
        database.child(user['localId']).child("Handle").set(FAN_name)
        database.child(user['localId']).child("ID").set(user['localId'])
        lit.title(FAN_name + " Welcome to the Gang")
        lit.write("You can now login to your account to get started.")
        go_login=lit.button("Login")
        if go_login:
            switch_page("a fang login")