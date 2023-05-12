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


## ______________________________________________________________________________________________________________________##

## This is the launch page Layout - each tab calls a different function displaying the various features
def launch():
    lit.write('--------------------')
    tab1, tab2, tab3, tab4, tab5, tab6 = lit.tabs(["What is FANG","|  CyberSecurity Tips","|  Learn More about Home Network Cybersecurity ","|  See How they can attack your network", "|  Who are we", "| testing some code"])

    with tab1: # What is FANG

            launch_pages.launch_tabs.what.what()

    with tab2: # Displaying tips and tricks on good cyberHygiene
            
            
            launch_pages.launch_tabs.tips.tips_lit()

    with tab3: # Displaying educational topics for users on networking and cybersecurity           

            launch_pages.launch_tabs.learn.learn_lit()

    with tab4: # Displaying a test for users to show their vulnerabilties
            
            launch_pages.launch_tabs.test.attacks_lit()

    with tab5: # Displaying a bit more about the team
            launch_pages.launch_tabs.who.who()

    with tab6: # This is a holding place to test a few scenarios and will  deleted at the end of development
                placeholder = lit.empty()

                input = placeholder.text_input('text', key=1)
                click_clear = lit.button('clear text input', key=3)
                if click_clear:
                        input = placeholder.text_input('text', value='', key=2)

                lit.write(input)
