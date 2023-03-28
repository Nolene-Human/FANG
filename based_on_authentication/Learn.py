
#import dependancies
import streamlit as lit
import Cyberhygiene.learn

# more streamlit imports
from streamlit_extras.switch_page_button import switch_page

# importing own functions
import Art.Animation.lottie_animations


# animation dependancies
from streamlit_lottie import st_lottie

# -- Streamlit Page Formatting -- # 
lit.set_page_config(page_title="Vulnerability Scanner", page_icon="*", layout="wide", initial_sidebar_state="expanded")

# -- Navigation bar
lit.markdown("# Learn ")


# -- Call the Lit Learn module from Cyberhygiene folder-- # 
Cyberhygiene.learn.learn_lit()


launch=Art.Animation.lottie_animations.load_animation("Art/Animation/launch.json")

st_lottie(
        launch,
        loop = True,
        height=200,
        width=200,
)

lit.markdown("#### Lets get started !")

test = lit.button("Take a quick test to see where your threats could lie")
if test:
    switch_page("Test")