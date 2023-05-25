
   ## ----------------------------------------THIS IS 'WHAT' TAB ------------------------------------------------------##
 ## -------------------------- Called from Launch.py when user select the test tab ------------------------------------##
 
# - FUTURE DEVELOPMENT - #
# - Add questionnaire so user are able to relate better to the treats 
# - Link each threat to a solution which will either be the TIPS or the SCANNER page 

# ______________________________________________________________________________________________________________________##

# - NO FUTURE DEVELOPEMENT PLANNED - #

import streamlit as lit
from PIL import Image #used to display images on page 
from streamlit_lottie import st_lottie
import Art.Animation.lottie_animations


def what():

  lit.markdown("**What is FANG**")
  lit.write("""
    Secure your network against cyber attacks and data breaches. We have developed an easy to use Zero Trust Network Cybersecurity Tool built on top of Cybersecurity cornerstones.\n
    Packing all the best practises of a corporate solution into an easy to use zero trust application of "never trust, always verify" approach to data access.\n 
    \n
    What does this mean? Every user and every device attempting to access your data is constantly authenticated and authorized, ensuring that only the right people have access to the right data at the right time.
    """)
  col1, col2 = lit.columns([1,6])
  with col2:
      lit.write("""
        **Our zero trust application offers several key features, which includes:**\n
      \n
      * Password Management Tool
      * Dashboard showing the activity on your network
      * Scanning tools to see who is on your network
      * a Tool to create a strong Cybersecurity Plan for your home business
      * Tools and training to secure your network against the most common attacks    
      """)
  
  with col1:
     what=Art.Animation.lottie_animations.load_animation("Art/Animation/cybersecurity.json")
     st_lottie(
     what,
     speed=1,
      loop=True,
      height = 150
     )
