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

## ______________________________________________________________________________________________________________________##

## Page UI / UX
lit.set_page_config(page_title="FANG",
        page_icon="🚀",
        layout="wide")

logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")

## ______________________________________________________________________________________________________________________##


## Side Bar Navigation
choice=lit.sidebar.selectbox('Welcome to FANG',['Home','Register','Login',"Reset Password",'Logout'])

## ______________________________________________________________________________________________________________________##

## Side Bar and Navigation
if choice == 'Home':
        launch_pages.launch.launch()

if choice == 'Login':
     email = lit.sidebar.text_input("Please enter your registered email")
     password = lit.sidebar.text_input("Please enter your password",type='password')
     
     login = lit.sidebar.checkbox("Login")
          
     if login:
        
       Authentication.user_login.login(email,password)
       
if choice=="Reset Password":
        launch_pages.launch.launch()
        email=lit.sidebar.text_input("Please enter your email address")
        reset_pass=lit.sidebar.button("Reset password")

        if reset_pass:
                reset=Firebase.firebaseconfig.firebase_auth()
                reset.send_password_reset_email(email)
                lit.sidebar.write("Reset Password email has been sent")      

if choice == 'Register':
        Authentication.user_registration.register()

if choice == 'Logout':

        lit.sidebar.success("You are logged out")
        launch_pages.launch.launch()
        

        