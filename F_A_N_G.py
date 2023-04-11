
# importing front end tool streamlit
import streamlit as lit
from PIL import Image


        #ANIMATION




from streamlit_extras.switch_page_button import switch_page



        # PAGE UI 
lit.set_page_config(page_title="a Fan of the FAM",page_icon='🚀', layout="wide")

logo=Image.open("Art/Pictures/banner.png")
lit.image(logo,caption="It's all for show productions")



        # HEADER
lit.markdown("---")

tab1, tab2, tab3, tab4, tab5 = lit.tabs(["What is FANG","|  CyberSecurity Tips","|  Learn More about Home Network Cybersecurity ","|  See How they can attack your network", "|  Who are we"])

with tab1:
        lit.write("F A N G is a Family area network cybersecurity tool that will help you secure your home network against the most common threats.")
        lit.write("We have developed a tool that is easy to use with the power of a corporate solution.")

with tab2:
        
        import Cyberhygiene.tips

        #Navigation
        lit.markdown("# Good CyberHygiene Tecniques + Tips")
        # -- Call the Lit tips module from Cyberhygiene folder -- # 
        Cyberhygiene.tips.tips_lit()

with tab3:
        import Cyberhygiene.learn

        lit.markdown("# Why are you under attack, and how FANG can help you secure your network")
        Cyberhygiene.learn.learn_lit()

with tab4:
        import Cyberhygiene.attacks

        lit.markdown("Ticks the boxes that get used in your house")

        Cyberhygiene.attacks.attacks_lit()

with tab5:
        lit.header("One Determined Human")