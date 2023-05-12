
#import dependancies
import streamlit as lit
import Cyberhygiene.attacks




# -- Streamlit Page Formatting -- # 
lit.set_page_config(page_title="Vulnerability Scanner", page_icon="*", layout="wide", initial_sidebar_state="expanded")

# -- Navigation bar
lit.markdown("# Test ")


# -- Call the Lit Learn module from Cyberhygiene folder-- # 
Cyberhygiene.attacks.attacks_lit()