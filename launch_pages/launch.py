


import streamlit as lit

import launch_pages.launch_tabs.learn
import launch_pages.launch_tabs.test
import launch_pages.launch_tabs.tips
import launch_pages.launch_tabs.what
import launch_pages.launch_tabs.who

def launch():
    lit.write('--------------------')
    tab1, tab2, tab3, tab4, tab5, tab6 = lit.tabs(["What is FANG","|  CyberSecurity Tips","|  Learn More about Home Network Cybersecurity ","|  See How they can attack your network", "|  Who are we", "| testing some code"])

    with tab1:

            launch_pages.launch_tabs.what.what()

    with tab2:
                
            lit.markdown("# Good CyberHygiene Tecniques + Tips")
            launch_pages.launch_tabs.tips.tips_lit()

    with tab3:           

            lit.markdown("# Why are you under attack, and how FANG can help you secure your network")
            launch_pages.launch_tabs.learn.learn_lit()

    with tab4:
            launch_pages.launch_tabs.test.attacks_lit()

    with tab5:
            launch_pages.launch_tabs.who.who()

    with tab6:
                placeholder = lit.empty()

                input = placeholder.text_input('text', key=1)
                click_clear = lit.button('clear text input', key=3)
                if click_clear:
                        input = placeholder.text_input('text', value='', key=2)

                lit.write(input)