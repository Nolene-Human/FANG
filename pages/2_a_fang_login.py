import streamlit as lit
from PIL import Image


lit.set_page_config(page_title="FANG Login",page_icon='🚀', layout="wide")

import Authentication.login_functions


logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")

Authentication.login_functions.user_login()

