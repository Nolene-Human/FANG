


import streamlit as lit

import launch_pages.launch_tabs.learn
import launch_pages.launch_tabs.test
import launch_pages.launch_tabs.tips
import launch_pages.launch_tabs.what
import launch_pages.launch_tabs.who

def launch():
    lit.write('--------------------')
    tab1, tab2, tab3, tab4, tab5 = lit.tabs(["What is FANG","|  CyberSecurity Tips","|  Learn More about Home Network Cybersecurity ","|  See How they can attack your network", "|  Who are we"])

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