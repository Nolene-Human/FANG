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
import registered_pages.register

## ______________________________________________________________________________________________________________________##


## Importing Firebase back end servcie SDK's ##
import Firebase.firebaseconfig

## ______________________________________________________________________________________________________________________##

## Page UI / UX
lit.set_page_config(page_title="FANG",
        page_icon="🚀",
        layout="wide")

logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")

## ______________________________________________________________________________________________________________________##

this_user=Authentication.user_login.return_this_user()

## Side Bar and Navigation
home=lit.sidebar.radio("""**WELCOME**""",['Home','Login /Register','Registered Users'])

## ______________________________________________________________________________________________________________________##

if 'loggedIn' not in lit.session_state:
                lit.session_state['loggedIn']=False

if home == 'Login /Register':

        login, register, reset = lit.tabs(["|  Login","|  Register", "|  Reset Password"])
        
        with login:
                Authentication.user_login.login_form()

        with register:
                form, notes = lit.columns(2)
                with form:
                        Authentication.user_registration.registration_form()
                with notes:
                        Authentication.user_registration.registration_messages()
        with reset:
                Authentication.user_login.reset_password()

elif home == 'Registered Users':
        
        # managing session state for logged in users
        if lit.session_state['loggedIn']:
                logout=lit.sidebar.button("logout")
                registered_pages.register.dashboard()

                if logout:
                        
                        this_user.clear()
                        lit.session_state['loggedIn']=False
                        lit.cache_data.clear()
                        
                       
        else:
                lit.write("You need to be logged in to view this page")

## ______________________________________________________________________________________________________________________##
        
else:
      launch_pages.launch.launch()  

        