import streamlit as lit
import Cyberhygiene.tips

# animation dependancies
from streamlit_lottie import st_lottie

# importing own functions
import Art.Animation.lottie_animations

# -- Streamlit Page Formatting -- # 
lit.set_page_config(page_title="Vulnerability Scanner", page_icon="*", layout="wide", initial_sidebar_state="expanded")



#Navigation
lit.markdown("# Good CyberHygiene Tecniques + Tips")


ex_robot=Art.Animation.lottie_animations.load_animation("Art/Animation/excited_robot.json")

st_lottie(
        ex_robot,
        loop = True,
        height=200,
        width=200,
)

# -- Call the Lit tips module from Cyberhygiene folder -- # 
Cyberhygiene.tips.tips_lit()