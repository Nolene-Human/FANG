

   ## ----------------------------------------THIS IS 'MAIN' ------------------------------------------------------##
 ## ----------------------------Launced and the only 'page in this application-----------------------------------------##
## ---------------All other 'pages' are called functions displayed when conditions have been met-------------------------##

# - NO FUTURE DEVELOPMENT PLANNED - #

## ______________________________________________________________________________________________________________________##

## Importing Front-end tool Streamlit (https://streamlit.io/)
import streamlit as lit
from PIL import Image #used to display images on page

## ______________________________________________________________________________________________________________________##

## Import applications Login and Registration Functions ##
import launch_pages.launch


## ______________________________________________________________________________________________________________________##

## Page UI / UX
lit.set_page_config(page_title="FANG",
        page_icon="🚀",
        layout="wide")

logo=Image.open("Art/Pictures/logo.png")
lit.image(logo,caption="It's all for show productions")

## ______________________________________________________________________________________________________________________##

launch_pages.launch.launch()
