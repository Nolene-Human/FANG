import streamlit as lit

import Scanners.configscan

# more streamlit imports
from streamlit_extras.switch_page_button import switch_page


# -- Page UI -- #
lit.set_page_config(page_title="Vulnerability Scanner", page_icon="*", layout="wide", initial_sidebar_state="expanded")



# -- Sharing session states across multi pages as information will need to be re-used on other pages depending on the scan -- #
# -- This is saving the gateway ip address from user input -- #
if "gateway" not in lit.session_state:
    lit.session_state["gateway"]=""

gateway = lit.text_input("Enter your Gateway address and save it for further scanning : ", lit.session_state["gateway"])


# -- button is saving the result in the session state -- #
confirm_gateway = lit.button("Save it")

lit.markdown("---")

if confirm_gateway:
    lit.session_state["gateway"] = gateway
    port = lit.button("Great, you are ready to scan for open ports")
    if port:
        switch_page("Port_Scanner")



# -- Load IPCONFIG function is auto called when page load -- #
Scanners.configscan.config_lit()




