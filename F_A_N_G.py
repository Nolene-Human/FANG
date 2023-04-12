
# importing front end tool streamlit
import streamlit as lit
from PIL import Image


import launch_pages.learn
import launch_pages.register
import launch_pages.test
import launch_pages.tips
import launch_pages.what
import launch_pages.who


from streamlit_extras.switch_page_button import switch_page


logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")


register_now=lit.sidebar.button("Register Now")
if register_now:
        launch_pages.register.register()

else:
        # HEADER
        lit.markdown("---")

        tab1, tab2, tab3, tab4, tab5 = lit.tabs(["What is FANG","|  CyberSecurity Tips","|  Learn More about Home Network Cybersecurity ","|  See How they can attack your network", "|  Who are we"])

        with tab1:

                launch_pages.what.what()

        with tab2:
                
                import launch_pages.tips

                lit.markdown("# Good CyberHygiene Tecniques + Tips")
                launch_pages.tips.tips_lit()

        with tab3:
                import launch_pages.learn

                lit.markdown("# Why are you under attack, and how FANG can help you secure your network")
                launch_pages.learn.learn_lit()

        with tab4:
                import launch_pages.test
                launch_pages.test.attacks_lit()

        with tab5:
                import launch_pages.who
                launch_pages.who.who()