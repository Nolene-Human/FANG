
import streamlit as lit
from PIL import Image





lit.set_page_config(page_title="Register for a FANG Account ",page_icon='🚀', layout="wide")

logo=Image.open("Art/Pictures/banner.png")
lit.image(logo,caption="It's all for show productions")


lit.header("You are now logged out")
