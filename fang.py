## ----------------------------------------THIS IS 'MAIN' ----------------------------------------------- ##
## ----------Launced when application start and is the only 'page' in this application------------------##
## --------All other 'pages' are called functions displayed when conditions have been met-------------##

## ______________________________________________________________________________________________________________________##

## Importing Front-end tool Streamlit (https://streamlit.io/)
import streamlit as lit
from PIL import Image #used to display images on page

## ______________________________________________________________________________________________________________________##

## Import applications Login and Registration Functions ##
import launch_pages.launch
import Authentication.user_registration
import Authentication.user_login 

## ______________________________________________________________________________________________________________________##

## Page UI / UX
lit.set_page_config(page_title="FANG",
        page_icon="🚀",
        layout="wide")

logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")

## ______________________________________________________________________________________________________________________##
   
## Side Bar and Navigation
home=lit.sidebar.radio("""**WELCOME**""",['Home','Login /Register','Registered Users'])

## ______________________________________________________________________________________________________________________##

if home == 'Login /Register':

        login, register, reset = lit.tabs(["|  Login","|  Register", "|  Reset Password"])
        
        with login:
                Authentication.user_login.login_form()

        with register:
                Authentication.user_registration.registration_form()

        with reset:
                Authentication.user_login.reset_password()

elif home == 'Registered Users':
        lit.write("You need to be registered to view this page")

else:
      launch_pages.launch.launch()  

        