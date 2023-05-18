## ----------------------------------------THIS IS 'MAIN' ----------------------------------------------- ##
## ----------Launced when application start and is the only 'page' in this application------------------##
## --------All other 'pages' are called functions displayed when conditions have been met-------------##

# - NO FUTURE DEVELOPMENT PLANNED - #

## ______________________________________________________________________________________________________________________##

## Importing Front-end tool Streamlit (https://streamlit.io/)
import streamlit as lit
from PIL import Image #used to display images on page

## ______________________________________________________________________________________________________________________##

## Import applications Login and Registration Functions ##
import launch_pages.launch
import Authentication.user_registration
import Authentication.user_login
import Firebase.firebaseconfig
import Authentication.mfa

import Authentication.loginform 
import requests

auth= Firebase.firebaseconfig.firebase_auth()
database=Firebase.firebaseconfig.firebase_database()



## ______________________________________________________________________________________________________________________##

## Page UI / UX
lit.set_page_config(page_title="FANG",
        page_icon="🚀",
        layout="wide")

logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")

## ______________________________________________________________________________________________________________________##
   
## Side Bar and Navigation
home=lit.sidebar.radio("""**WELCOME**""",['Home','Register','Login',"Reset Password"],key="visible")


## ______________________________________________________________________________________________________________________##


if home == 'Login':       
 
        email = lit.sidebar.text_input("Please enter your registered email")
        password = lit.sidebar.text_input("Please enter your password",type='password')
        
        lit.sidebar.markdown("---")  
       
        login = lit.sidebar.checkbox("Login",)
        
        if login:

                try:
                        user=auth.sign_in_with_email_and_password(email,password)
                        new_OTP=name=database.child(user['localId']).child('Userkey').get().val()
                        generated_OTP=Authentication.mfa.generatepin(new_OTP)
                        entered_OTP=lit.sidebar.text_input("Enter your one time passcode: ")

                        verify_OTP=lit.sidebar.checkbox("Verify")
                        if verify_OTP:
                                lit.write(generated_OTP)
                                if generated_OTP == entered_OTP:
                                        lit.header("Welcome to your home page")
                                        logged_in=lit.sidebar.checkbox("",['Logout'], label_visibility="collapsed")
                                        if logged_in=="Logout":
                                                launch_pages.launch.launch()
                                                lit.sidebar.success("You are logged out")

                                else:
                                        lit.write("codes did not match")               
                except requests.exceptions.HTTPError as err:
                                lit.write(err)
                                lit.error("There is a problem with the details you entered, please retry.")  
                                lit.subheader("""Forgot your password?
                                You can reset your password in the drop down list""")  
                                

                       
elif home=="Reset Password":
                launch_pages.launch.launch()
                email=lit.sidebar.text_input("Please enter your email address")
                reset_pass=lit.sidebar.button("Reset password")

                if reset_pass:
                        reset=Firebase.firebaseconfig.firebase_auth()
                        reset.send_password_reset_email(email, action_code_settings=None)
                        lit.sidebar.write("Reset Password email has been sent") 
                        

elif home == 'Register':
        Authentication.user_registration.register()



else:
      launch_pages.launch.launch()  

        