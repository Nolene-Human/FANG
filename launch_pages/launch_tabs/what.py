
   ## ----------------------------------------THIS IS 'WHAT' TAB ------------------------------------------------------##
 ## -------------------------- Called from Launch.py when user select the test tab ------------------------------------##
 
# - FUTURE DEVELOPMENT - #
# - Add questionnaire so user are able to relate better to the treats 
# - Link each threat to a solution which will either be the TIPS or the SCANNER page 

# ______________________________________________________________________________________________________________________##

# - NO FUTURE DEVELOPEMENT PLANNED - #

import streamlit as lit
from PIL import Image #used to display images on page 

def what():
        
    col1,colb=lit.columns([2,6])

    triangle=Image.open("Art/Pictures/triangle.png")
    col1.image(triangle)
    
    colb.write("""
    Secure your network against cyber attacks and data breaches. We have developed an easy to use Zero Trust Network Cybersecurity Tool built on top of Cybersecurity cornerstones.\n
    Packing all the best practises of a corporate solution into an easy to use zero trust application of "never trust, always verify" approach to data access.\n 
    \n
    What does this mean? Every user and every device attempting to access your data is constantly authenticated and authorized, ensuring that only the right people have access to the right data at the right time.

    Our zero trust application offers several key features, which includes:\n
    \n
    * Password Management Tool
    * Dashboard showing the activity on your network
    * Scanning tools to see who is on your network
    * Cybersecurity Plan tool to keep your customers at piece you are Cyber strong
    * Tools to secure your network against the most common attacks    
    """)
    