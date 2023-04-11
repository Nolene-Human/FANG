import streamlit as lit
from PIL import Image

import Authentication.login_functions



lit.set_page_config(page_title="Login to FANG ",page_icon='🚀', layout="wide")

logo=Image.open("Art/Pictures/banner.png")
lit.image(logo,caption="It's all for show productions")


#Authentication.login_functions.user_login()

lit.header("Verification")

lit.text_input("Please enter verification code : ")

lit.button("Verify")

