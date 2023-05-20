   ## ----------------------------------------THIS IS 'LAUNCH PAGE LAYOUT' ------------------------------------------------------##
 ## -------------------------- Called from registration and login when user select register ------------------------------------##
## -------------------------- Uses Firebase_Config functions to verify and register a new users -------------------------------##

# - NO FUTURE DEVELOPMENT PLANNED - #

## ______________________________________________________________________________________________________________________##

import streamlit as lit

## ______________________________________________________________________________________________________________________##

# Each function accessable under a different TAB by unregistered users

import launch_pages.launch_tabs.learn
import launch_pages.launch_tabs.test
import launch_pages.launch_tabs.tips
import launch_pages.launch_tabs.what
import launch_pages.launch_tabs.who
import launch_pages.launch_tabs.testintro


## ______________________________________________________________________________________________________________________##

## This is the launch page Layout - each tab calls a different function displaying the various features
def launch():
        tab1, tab2, tab3, tab4, tab5, tab6 = lit.tabs(["Introduction","|   What is FANG","|  CyberSecurity Tips","|  Learn Home Cybersecurity ","|  Take the Vulnerability Test", "|  Who are we"])

        with tab1:
                launch_pages.launch_tabs.testintro.testing1()

        with tab2: # What is FANG

            launch_pages.launch_tabs.what.what()

        with tab3: # Displaying tips and tricks on good cyberHygiene
            
            
            launch_pages.launch_tabs.tips.tips()

        with tab4: # Displaying educational topics for users on networking and cybersecurity           

            launch_pages.launch_tabs.learn.learn()

        with tab5: # Displaying a test for users to show their vulnerabilties
            
            launch_pages.launch_tabs.test.test()

        with tab6: # Displaying a bit more about the team
            launch_pages.launch_tabs.who.who()

    
