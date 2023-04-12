import streamlit as lit
from PIL import Image


lit.set_page_config(page_title="LOGIN",
        page_icon="🚀",
        layout="wide")

import Authentication.login_functions


logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")

lit.sidebar.button("Register")
lit.sidebar.button("Reset Password")


Authentication.login_functions.user_login()

