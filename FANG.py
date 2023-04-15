
# importing front end tool streamlit
import streamlit as lit
from PIL import Image


import Authentication.user_registration
import Authentication.login_functions


lit.set_page_config(page_title="FANG",
        page_icon="🚀",
        layout="wide")

logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")

choice=lit.sidebar.selectbox('Login/Register',['Login','Register'])

if choice == 'Login':
        Authentication.login_functions.user_login()

if choice == 'Register':
        Authentication.user_registration.register()
