

   ## ----------------------------------------THIS IS 'MAIN' ------------------------------------------------------##
 ## ----------------------------Launced and the only 'page in this application-----------------------------------------##
## ---------------All other 'pages' are called functions displayed when conditions have been met-------------------------##

# - NO FUTURE DEVELOPMENT PLANNED - #

## ______________________________________________________________________________________________________________________##

## Importing Front-end tool Streamlit (https://streamlit.io/)
import streamlit as lit
from PIL import Image #used to display images on page

## ______________________________________________________________________________________________________________________##

## Import applications Login and Registration Functions ##

import Authentication.registration
import Authentication.login

## ______________________________________________________________________________________________________________________##

## Page UI / UX
lit.set_page_config(page_title="FANG",
        page_icon="🚀",
        layout="wide")

logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")

## ______________________________________________________________________________________________________________________##

## Side Bar Navigation
choice=lit.sidebar.selectbox('Login/Register',['Login','Register'])

## ______________________________________________________________________________________________________________________##

## Side Bar and Navigation
if choice == 'Login':
        Authentication.login.login()

if choice == 'Register':
        Authentication.registration.register()